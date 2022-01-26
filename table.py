import pandas as pd
import io
import os
import info
import qrcode
from string import ascii_letters, digits
from typing import List
from random import choices

class Table:
    id: int
    tableId: str
    URL: str
    requests: List[int]
    infoClients: pd.DataFrame
    QRCode: io.StringIO

    def __init__(self) -> None:
        self.infoClients = pd.read_csv("tables.csv", sep=';')
        self.id = self.infoClients.__len__()
        
        self.tableId = ''.join(choices(ascii_letters + digits, k=8))
        os.system("mkdir tables/{}".format(self.tableId))
        os.system("cp -R {}/* tables/{}".format(info.WEBSITEFOLDER, self.tableId))
        
        self.requests = list()
        self.URL = 'http://{}:{}/tables/{}/'.format(info.my_ip, info.PORT, self.tableId)
        
        qr = qrcode.QRCode()
        qr.add_data(self.URL)
        
        self.QRCode = io.StringIO()
        qr.print_ascii(out=self.QRCode)
            
        self.update_tables()
        pass   
    def __str__(self, QR: bool) -> str:
        self.infoClients = pd.read_csv("tables.csv", sep=';')
        str =  self.infoClients.iloc[self.id].to_string()
        if (QR):
            self.QRCode.seek(0)
            return str + self.QRCode.read()
        else: return str        
    def update_tables(self) -> None:
        with open("tables.csv", "a") as f:
            f.write('{};{};{}\n'.format(self.id, self.tableId, self.URL))

if __name__ == "__main__":
    x = Table()
    print(x.__str__(QR=True))
    pass