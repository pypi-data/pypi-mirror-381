#!/bin/python

import random
import string
import re
import time
import os
import json
import gspread
from google.oauth2.service_account import Credentials

from .task import MBIOTask
from .xmlconfig import XMLConfig


# Principe de base gspread API
# ----------------------------
# https://console.cloud.google.com/
# Créer un projet
# Dans les API, activer l'API "Google Sheets API"
# Dans les Identifiants, créer un "compte de service"
# Dans le compte de service, sous "clés" ajouter une clé JSON (récupérer le fichier auth .json)
# Récupérer l'email du compte de service (disponible dans le fichier .json) et partager la feuille Google Sheet avec cette adresse
# Récupérer l'id de la sheet (dispo dans l'URL) pour utilisation comme paramètre key dans l'appel .spreadsheet(key=xxx)

# gs=GSheet('digimat-mbio-gapi.json')
# sheets=gs.spreadsheet('1plgD2LxWK5S6obV9ZUHPdwbSKEvCyhxj8h01FDT0h-M')
# sheet=sheets.get_worksheet(0)
# print(sheet.acell('a1').value)
# sheet.update_acell("A1", "HELLO")
# sheet.format("A1", {'textFormat': {'bold': True}})
# sheet.batch_get(["A1", "A5"])


class GSheet(object):
    def __init__(self, fname='digimat-mbio-gapi.json', readonly=False, timeout=15.0):
        self._fname=fname
        self._readonly=readonly
        self._timeout=timeout
        self._client=None
        self._timeoutApi=0
        self._delayApi=0

        self._spreadsheet=None
        self._idspreadsheet=None
        self._sheets=None
        self._sheetsById=None
        self._sheetsByIndex=None
        self._sheetsByName=None
        self.resetCache()

    def resetCache(self):
        self._sheets=[]
        self._sheetsById={}
        self._sheetsByIndex={}
        self._sheetsByName={}

    def sheet(self, key=0) -> gspread.worksheet.Worksheet:
        if self._spreadsheet and self._sheets:
            try:
                return self._sheetsById[key]
            except:
                pass
            try:
                return self._sheetsByIndex[key]
            except:
                pass
            try:
                return self._sheetsByName[key.lower()]
            except:
                pass

        return None

    def apiSleep(self, n=0):
        wait=(2 ** n) + random.random()
        time.sleep(wait)

    def batchget(self, addresses, retries=5):
        for n in range(retries):
            try:
                data={}
                spreadsheet=self.spreadsheet()
                r=spreadsheet.values_batch_get(addresses)['valueRanges']
                for item in r:
                    # address is something like "sheet!a1"
                    # or "mydata" in case of a named field
                    address=item['range'].lower()
                    address=address.replace("'", "")
                    values=item.get('values')
                    if values is not None:
                        value=item['values'][0][0]
                    else:
                        value=None
                    data[address]=value
                return data
            except gspread.exceptions.APIError as e:
                if "429" in str(e):
                    self.apiSleep(n)
            except:
                break
        return None

    def get(self, sheet, addresses, retries=5):
        for n in range(retries):
            try:
                worksheet=self.sheet(sheet)
                return worksheet.batch_get(addresses)
            except gspread.exceptions.APIError as e:
                if "429" in str(e):
                    self.apiSleep(n)
            except:
                break
        return None

    def batchset(self, data, retries=5):
        for n in range(retries):
            try:
                spreadsheet=self.spreadsheet()
                spreadsheet.values_batch_update(data)
                return True
            except gspread.exceptions.APIError as e:
                if "429" in str(e):
                    self.apiSleep(n)
            except:
                pass
        return False

    def set(self, sheet, data, retries=5):
        for n in range(retries):
            try:
                worksheet=self.sheet(sheet)
                worksheet.batch_update(data)
                return True
            except gspread.exceptions.APIError as e:
                if "429" in str(e):
                    self.apiSleep(n)
            except:
                pass
        return False

    def __getitem__(self, key):
        return self.sheet(key)

    def addSheet(self, sheet: gspread.worksheet.Worksheet) -> gspread.worksheet.Worksheet:
        if sheet:
            try:
                sid=sheet.id
                if not self.sheet(sid):
                    self._sheets.append(sheet)
                    self._sheetsById[sid]=sheet
                    self._sheetsByIndex[sheet.index]=sheet
                    self._sheetsByName[sheet.title.lower()]=sheet
            except:
                pass
        return sheet

    def retrieveSheets(self):
        self.resetCache()
        if self._spreadsheet:
            try:
                sheets=self._spreadsheet.worksheets()
                if sheets:
                    for sheet in sheets:
                        self.addSheet(sheet)
            except:
                pass
        return self._sheets

    def client(self) -> gspread.client.Client:
        if self._client:
            return self._client

        scope='https://www.googleapis.com/auth/spreadsheets'
        if self._readonly:
            scope+='.readonly'

        try:
            credentials=Credentials.from_service_account_file(self._fname, scopes=[scope])
            if credentials:
                client=gspread.authorize(credentials)
                if client:
                    client.set_timeout(self._timeout)
                    self._client=client
                    self._spreadsheet=None
                    self.resetCache()
        except:
            pass

        return self._client

    def auth(self):
        client=self.client()
        if client is not None:
            return True
        return False

    def reauth(self) -> gspread.client.Client:
        self._client=None
        self._spreadsheet=None
        self.resetCache()
        if self.auth():
            if self._idspreadsheet:
                self.spreadsheet(self._idspreadsheet)
            return self._client
        return None

    def spreadsheet(self, key=None) -> gspread.Spreadsheet:
        try:
            if key:
                if self._spreadsheet and self._spreadsheet.id==key:
                    return self._spreadsheet

                client=self.client()
                if client:
                    if 'https://' in key:
                        spreadsheet=client.open_by_url(key)
                    else:
                        spreadsheet=client.open_by_key(key)

                    if spreadsheet:
                        self._spreadsheet=spreadsheet
                        self._idspreadsheet=key
                        self.retrieveSheets()
                pass
        except:
            pass

        return self._spreadsheet

    def cell(self, sheet: gspread.worksheet.Worksheet, address) -> gspread.cell.Cell:
        try:
            if sheet and address:
                return sheet.acell(address)
        except:
            pass

    def __repr__(self):
        try:
            return '%s(%s, %d sheets)' % (self.__class__.__name__, self._spreadsheet.title, len(self._sheets))
        except:
            pass
        if self._sheets:
            return '%s(%s)' % (self.__class__.__name__, len(self._sheets))
        return '%s()' % (self.__class__.__name__)


class MBIOTaskGSheet(MBIOTask):
    def initName(self):
        return 'gs'

    def onInit(self):
        self.config.set('credentials', 'digimat-mbio-gapi.json')
        self.config.set('readonly', False)
        self.config.set('refreshperiod', 10)
        self.config.set('timeout', 10)
        self.config.set('id')
        self._timeoutRefresh=0
        self._timeoutSync=0
        self._timeoutRefreshNamedRanges=0
        self.valueDigital('comerr', default=False)
        self._sheets={}
        self._cells={}
        self._addresses={}
        self._namedRanges={}
        self._gsheet=None

    # Each sheet/cell must have a unique name (value name)
    def cell(self, name):
        name=name.lower()
        cell=self._cells.get(name)
        if cell:
            return cell
        return None

    # def cellValue(self, name):
        # cell=self.cell(name)
        # if cell:
            # return cell['value']
        # return None


    # TODO: pas de override pour AI --> add IMPORT item (cell->override-item) without mbio-value (must be writable)
    # pas de expression dans AO (uniquement writable) --> add EXPORT item (expression->cell) without mbio-value

    def isA1Notation(self, address: str) -> bool:
        return re.fullmatch(r"[A-Z]{1,3}+[1-9][0-9]*", address, re.IGNORECASE) is not None

    def declareAddress(self, sheet, cell):
        if sheet and cell:
            # allows for sheet!a1 notation or pure named field single string
            if self.isA1Notation(cell):
                address="%s!%s"  % (sheet['name'], cell)
            else:
                # named field
                address=cell

            address=address.lower()
            if not address in self._addresses:
                self._addresses[address]=None
            return address
        return None

    def loadCell(self, sheet, xml: XMLConfig, writable=True, digital=False, variables=None):
        if sheet:
            name=xml.get('name')
            name=self.replaceVariables(name, variables)

            address=xml.get('cell') or xml.get('address')
            address=self.replaceVariables(address, variables)

            if name and not self.cell(name) and address:
                self.declareAddress(sheet, address)
                retain=False
                storeunit=False
                if writable:
                    storeunit=xml.getBool('storeunit')
                else:
                    retain=xml.getBool('retain', True)

                vname='%s_%s' % (sheet['alias'], name)
                default=xml.getFloat('default')
                if digital:
                    value=self.valueDigital(vname, writable=writable, default=default, commissionable=True)
                else:
                    unit=xml.get('unit')
                    resolution=xml.getFloat('resolution', 0.1)
                    value=self.value(vname, unit=unit, resolution=resolution, writable=writable, default=default, commissionable=True)

                if retain:
                    try:
                        v=self.pickleRead('cell-%s-retain' % name)
                        if v is not None:
                            value.updateValue(v)
                    except:
                        pass

                xaddress=address
                if self.isA1Notation(address):
                    xaddress='%s!%s' % (sheet['name'], address)
                data={'name': name, 'sheet': sheet['name'],
                      'address': address, 'xaddress': xaddress,
                      'writable': writable, 'retain': retain,
                      'value': value}

                if writable:
                    self._sheets[sheet['name']]['writablecells'].append(name)
                    data['storeunit']=storeunit
                    # support for value expression calculations
                    self.loadValueExpression(value, xml, variables)

                self.logger.debug('Declaring GSheet(%s) CELL %s' % (self.config.id, name))
                self._cells[name]=data

                self._sheets[sheet['name']]['cells'].append(name)

                return data
        return None

    def loadSheet(self, name, xml: XMLConfig):
        sheet=self._sheets.get(name)
        if xml is not None and sheet is None:
            alias=xml.get('alias', name)
            self.logger.info('Declaring GSheet(%s-%s) SHEET %s (alias %s)' % (self.name, self.config.id, name, alias))
            sheet={'name': name, 'alias': alias, 'cells': [], 'writablecells': [], 'dumps': [], 'imports': [], 'exports': []}
            self._sheets[name]=sheet

            myvariables={'gsheet': self.name, 'sheetname': sheet['name'], 'sheetalias': sheet['alias']}

            items=xml.children('ai')
            if items:
                for item in items:
                    self.loadCell(sheet, item, writable=False, digital=False, variables=myvariables)
            items=xml.children('di')
            if items:
                for item in items:
                    self.loadCell(sheet, item, writable=False, digital=True, variables=myvariables)
            items=xml.children('ao')
            if items:
                for item in items:
                    self.loadCell(sheet, item, writable=True, digital=False, variables=myvariables)
            items=xml.children('do')
            if items:
                for item in items:
                    self.loadCell(sheet, item, writable=True, digital=True, variables=myvariables)

            items=xml.children('dump')
            if items:
                for item in items:
                    cell=item.get('cell')
                    key=item.get('key')
                    if cell and key:
                        refresh=item.getInt('refresh', 15, vmin=5)
                        data={'cell': cell, 'key': key, 'refresh': refresh, 'timeout': 0}
                        self.logger.info('Declaring GSheet(%s-%s) SHEET %s (alias %s) DUMP [%s]->%s' % (self.name, self.config.id, name, alias, key, cell))
                        sheet['dumps'].append(data)

            items=xml.children('import')
            if items:
                for item in items:
                    cell=item.get('cell')
                    key=item.get('key')
                    key=self.replaceVariables(key, myvariables)
                    if cell and key:
                        self.declareAddress(sheet, cell)
                        refresh=item.getInt('refresh', 15, vmin=5)
                        data={'cell': cell, 'key': key}
                        self.logger.info('Declaring GSheet(%s-%s) SHEET %s (alias %s) IMPORT %s->%s' % (self.name, self.config.id, name, alias, cell, key))
                        sheet['imports'].append(data)

            items=xml.children('export')
            if items:
                for item in items:
                    key=item.get('key')
                    key=self.replaceVariables(key, myvariables)
                    cell=item.get('cell')
                    if key and cell:
                        refresh=item.getInt('refresh', 15, vmin=5)
                        storeunit=item.getBool('storeunit', False)
                        data={'key': key, 'cell': cell, 'storeunit': storeunit}
                        self.logger.info('Declaring GSheet(%s-%s) SHEET %s (alias %s) EXPORT %s->%s' % (self.name, self.config.id, name, alias, key, cell))
                        sheet['exports'].append(data)

    def onLoad(self, xml: XMLConfig):
        self.config.update('credentials', xml.get('credentials'))
        self.config.update('readonly', xml.getBool('readonly'))
        self.config.update('refreshperiod', xml.getInt('refresh'))
        self.config.update('timeout', xml.getInt('timeout', vmin=3))
        self.config.update('id', xml.get('id'))
        if not self.config.id:
            self.config.update('id', self.pickleRead('id'))
        self.pickleWrite('id', self.config.id)

        # Remember that we are not online in this step !

        items=xml.children('sheet')
        if items:
            for item in items:
                name=item.get('name', 0)
                self.loadSheet(name, item)

    def credentials(self):
        fname=os.path.join(self.getMBIO().rootPath() or '.', self.config.credentials)
        fname=os.path.expanduser(fname)

        if not os.path.exists(fname):
            fname=os.path.join('/etc/sysconfig/digimat/credentials', self.config.credentials)

        if os.path.exists(fname):
            return fname

    def loadCredentialsData(self):
        fname=self.credentials()
        try:
            with open(fname) as f:
                data = json.load(f)
                return data
        except:
            pass

    def retrieveCredentialsServiceEmail(self):
        data=self.loadCredentialsData()
        try:
            return data['client_email']
        except:
            pass

    def gsheet(self, reset=False) -> GSheet:
        if reset or not self._gsheet:
            fname=self.credentials()
            if fname:
                self.logger.debug('Using GSheet(%s) credentials %s' % (self.name, fname))
                gs=GSheet(fname, readonly=self.config.readonly, timeout=self.config.timeout)
                self._gsheet=gs

        return self._gsheet

    def poweron(self):
        self.logger.info('Retrieving GSheet(%s-%s)' % (self.name, self.config.id))
        gs=self.gsheet(True)
        if gs:
            spreadsheet=gs.spreadsheet(self.config.id)
            if spreadsheet:
                self.logger.debug('Connected to GSheet(%s-%s) %s' % (self.name, self.config.id, gs))
                return True

        self.logger.error('Unable to retrieve GSheet(%s-%s)' % (self.name, self.config.id))
        return False

    def poweroff(self):
        self._gsheet=None
        return True

    def str2value(self, data):
        try:
            data=data.upper().replace(',', '.')
            if data=='TRUE':
                v=1.0
            elif data=='FALSE':
                v=0.0
            else:
                v=float(data)
            return v
        except:
            pass
        return None

    def addressFromNamedRange(self, name):
        try:
            return self._namedRanges[name.lower()]
        except:
            pass
        return name

    def col_to_a1(self, col_idx0: int) -> str:
        # 0 -> A, 25 -> Z, 26 -> AA ...
        col = ""
        n = col_idx0 + 1
        while n:
            n, r = divmod(n - 1, 26)
            col = chr(65 + r) + col
        return col

    def gridRangeToCellAddress(self, sheet, gr):
        try:
            # sheetId is implicitely 0 if not specified!
            sC = gr.get("startColumnIndex")
            sR = gr.get("startRowIndex")
            eC = gr.get("endColumnIndex")
            eR = gr.get("endRowIndex")

            if sR is None or sC is None:
                return None

            if eR is None: eR = sR + 1
            if eC is None: eC = sC + 1

            def cell(r0, c0):
                return f"{self.col_to_a1(c0)}{r0+1}"

            start = cell(sR, sC)
            end   = cell(eR - 1, eC - 1)
            if start == end:
                return f"{sheet.title}!{start}"
        except:
            self.logger.exception('x')
            pass
        return None

    def reloadNamedRanges(self):
        self.logger.debug('Reloading GSheet(%s) named ranges' % self.name)
        self._timeoutRefreshNamedRanges=self.timeout(180)

        gs=self.gsheet()
        spreadsheet=gs.spreadsheet()
        items=spreadsheet.list_named_ranges()
        # self.logger.warning(items)

        if items:
            self._namedRanges={}
            try:
                for nr in items:
                    name=nr.get('name').lower()
                    gr=nr.get('range')
                    sid=gr.get('sheetId', 0)
                    sheet=gs.sheet(sid)
                    address=self.gridRangeToCellAddress(sheet, gr)
                    if name and address:
                        self._namedRanges[name]=address.lower()

                self._timeoutRefreshNamedRanges=self.timeout(60)
            except:
                pass

    """
    def sheetExportManager(self) -> bool:
        result=True

        # collect all cells with pending sync
        addresses=[]

        # prepare data that need to be sent (pushed) to the sheet
        data=[]

        # EXPORTS (key->cell maping without using mbio values)
        for export in sheets['exports']:
            self.microsleep()
            if not self.isTimeout(export['timeout']):
                continue

            export['timeout']=self.timeout(export['period'])
            address=export['cell']
            if not address in addresses:
                addresses.append(address)
                key=export['key']
                value=self.getMBIO().value(key)
                if value is not None:
                    data.append({'range': address, 'values': [[value.value]]})
                    if export['storeunit']:
                        row,col=gspread.utils.a1_to_rowcol(address)
                        col+=1
                        address=gspread.utils.rowcol_to_a1(row, col)
                        data.append({'range': address, 'values': [[value.unitstr()]]})

        if data:
            # push the data in one request
            self.logger.debug('Write cells %s!%s to GSheet(%s)' % (sheet['name'], addresses, self.name))

            gs=self.gsheet()
            result=gs.set(sheet['name'], data)

            # inhibit the gsheet sync for a time
            self._timeoutSync=self.timeout(5)

            # force a value refresh after sync
            self._timeoutRefresh=0

            for name in cells:
                cell=self.cell(name)
                value=cell['value']
                if result:
                    value.clearSync()
                    value.setError(False)
                else:
                    value.setError(True)

        return result






                override=cell['override']
                try:
                    v=self.str2value(data[n][0][0])
                    if v is not None:
                        value.updateValue(v)
                        value.setError(False)
                        if override is not None:
                            ovalue=self.getMBIO().value(override)
                            if ovalue is not None:
                                ovalue.manual(v)
                        if cell['retain']:
                            self.pickleWrite('cell-%s-retain' % cell['name'], v)
                        continue
                except:
                    pass

                if override is not None:
                    ovalue=self.getMBIO().value(override)
                    if ovalue is not None:
                        ovalue.auto()

    """

    def sheetImportManager(self, sheet) -> bool:
        result=True

        for item in sheet['imports']:
            address=self.addressFromNamedRange(item['cell'])
            if self.isA1Notation(address):
                address='%s!%s' % (sheet['name'], address)
            v=self._addresses.get(address)

            value=self.getMBIO().value(item['key'])
            self.logger.warning("IMPORT %s:%s --> %s" % (address, v, value))

            if value is not None:
                if v is not None:
                    value.manual(v)
                else:
                    value.auto()
                continue

        return result

    def sheetSyncManager(self, sheet) -> bool:
        result=True

        self._timeoutSync=self.timeout(1)

        # collect all cells with pending sync
        addresses=[]
        cells=sheet['writablecells']

        if not cells:
            return True

        # prepare data that need to be sent (pushed) to the sheet
        data=[]

        # AO, DO
        for name in cells:
            self.microsleep()
            cell=self.cell(name)
            value=cell['value']
            self.evalValueExpression(value)

            if value.isPendingSync():
                addresses.append(cell['address'])
                data.append({'range': cell['address'], 'values': [[value.toReachValue]]})
                if cell['storeunit']:
                    row,col=gspread.utils.a1_to_rowcol(cell['address'])
                    col+=1
                    address=gspread.utils.rowcol_to_a1(row, col)
                    data.append({'range': address, 'values': [[value.unitstr()]]})

        """
        # EXPORTS (key->cell maping without using mbio values)
        for export in sheets['exports']:
            self.microsleep()
            if not self.isTimeout(export['timeout']):
                continue

            export['timeout']=self.timeout(export['period'])
            address=export['cell']
            if not address in addresses:
                addresses.append(address)
                key=export['key']
                value=self.getMBIO().value(key)
                if value is not None:
                    data.append({'range': address, 'values': [[value.value]]})
                    if export['storeunit']:
                        row,col=gspread.utils.a1_to_rowcol(address)
                        col+=1
                        address=gspread.utils.rowcol_to_a1(row, col)
                        data.append({'range': address, 'values': [[value.unitstr()]]})
        """

        if data:
            # push the data in one request
            self.logger.debug('Write cells %s!%s to GSheet(%s)' % (sheet['name'], addresses, self.name))

            gs=self.gsheet()
            result=gs.set(sheet['name'], data)

            # inhibit the gsheet sync for a time
            if result:
                self._timeoutSync=self.timeout(5)
            else:
                self._timeoutSync=self.timeout(15)

            # force a value refresh after sync
            self._timeoutRefresh=0

            for name in cells:
                cell=self.cell(name)
                value=cell['value']
                if result:
                    value.clearSync()
                    value.setError(False)
                else:
                    value.setError(True)

        return result

    # TODO: to be integrated in syncSheetManager (allowing using only one request)
    def sheetDumpManager(self, sheet):
        gs=self.gsheet()
        for dump in sheet['dumps']:
            self.microsleep()
            if not self.isTimeout(dump['timeout']):
                continue

            values=self.getMBIO().values(dump['key'])
            address=dump['cell']
            row,col=gspread.utils.a1_to_rowcol(address)
            if values:
                data=[]
                for value in values:
                    iotag=''
                    if value.config.iomaptag:
                        iotag=value.config.iomaptag
                    data.append({'range': address, 'values': [[value.key, iotag, value.value, value.unitstr(), value.flags]]})
                    row+=1
                    address=gspread.utils.rowcol_to_a1(row, col)
                if data:
                    self.logger.debug('Dumping %s(%s) from GSheet(%s) to %s' % (sheet['name'], dump['key'], self.name, dump['cell']))
                    gs.set(sheet['name'], data)
                    dump['timeout']=self.timeout(dump['refresh'])

    def sheetManager(self, sheet) -> bool:
        result=True

        # process sheet "imports"
        if sheet['imports']:
            self.microsleep()
            self.sheetImportManager(sheet)

        # process sheet "dumps"
        if sheet['dumps']:
            self.microsleep()
            self.sheetDumpManager(sheet)

        return result

    def run(self):
        result=True

        if self.isTimeout(self._timeoutRefreshNamedRanges):
            self.reloadNamedRanges()

        if self.isTimeout(self._timeoutSync):
            for sheet in self._sheets.values():
                self.microsleep()
                if not self.sheetSyncManager(sheet):
                    result=False

        # refresh spreadsheet cells values (read values from spreadsheet)
        if self.config.refreshperiod>0 and self.isTimeout(self._timeoutRefresh):
            self._timeoutRefresh=self.timeout(self.config.refreshperiod)

            if self._addresses:
                gs=self.gsheet()
                addresses=[x for x in self._addresses.keys()]
                self.logger.debug('Retrieve cells %s from GSheet(%s)' % (addresses, self.name))
                data=gs.batchget(addresses)
                if data:
                    # reset values
                    for address in self._addresses:
                        self._addresses[address]=None

                    # self.logger.warning(data)
                    for address in data:
                        v=self.str2value(data[address])
                        self._addresses[address]=v

            # update values
            for cell in self._cells.values():
                address=self.addressFromNamedRange(cell['xaddress'])
                value=cell['value']

                v=self._addresses.get(address)
                if v is not None:
                    value.updateValue(v)
                    value.setError(False)
                    if cell['retain']:
                        self.pickleWrite('cell-%s-retain' % cell['name'], v)
                    continue

                value.setError(True)
                result=False

        for sheet in self._sheets.values():
            self.microsleep()
            if not self.sheetManager(sheet):
                result=False

        # FIXME: not accurate way to do it
        self.values.comerr.updateValue(not result)
        return 5.0

    @property
    def sid(self):
        return self.config.id

    def setSheetId(self, sid):
        if sid:
            self.logger.info('Remap sheet id to %s...' % sid)
            self.pickleWrite('id', sid)
            self.config.id=sid
            self.reset()
