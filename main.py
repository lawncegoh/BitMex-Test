from bitmex_websocket import BitMEXWebsocket
from pymongo import MongoClient

class Main():
    def __init__(self):
        self.ws = BitMEXWebsocket(
            endpoint="wss://www.bitmex.com/realtime", 
            symbol="XBTUSD", 
            api_key='68_LZNeK1m7TEwnksVTe_7ig', 
            api_secret='wKJXpjr6Y28BNDF4G97TBevkzLG0HVOurFDBn2dx42Sf_Aga'
        )

        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.main_database

        self.order_book = self.db.orderbook
        self.position = self.db.position
        self.balance = self.db.balance

        
        #uncomment these 3 methods to check out the db

        #to see orderbooks
        #self.check_db(self.find_all_orderbook())

        #to see position
        #self.check_db(self.find_all_positions())

        #to see balance
        #self.check_db(self.find_all_balance())

        self.__on_open()
        self.fetch_data()

    def check_db(self, objects):
        for object in objects:
            self.logger(object)

    def logger(self, object):
        print(object)

    def find_all_positions(self):
        # Returns a list
        return self.position.find({})

    def find_all_balance(self):
        # Returns a list
        return self.balance.find({})

    def find_all_orderbook(self):
        # Returns a list
        return self.order_book.find({})

    def list_db_collections(self):
        return self.db.list_collection_names()

    def __on_open(self):
        # Called when the WS opens.
        self.logger("Websocket Opened.")

    def __on_close(self):
        # Called on websocket close.
        self.logger('Websocket Closed')

    def fetch_data(self):
        # Balance
        funds = self.ws.funds()

        # Position
        positions = self.ws.recent_trades()

        # Order Book
        orderbook = self.ws.market_depth()

        self.__on_close(funds, positions, orderbook)

    def __on_open(self):
        '''Called when the WS opens.'''
        self.logger("Websocket Opened.")

    def __on_close(self, funds, positions, orderbook):
        '''Called on websocket close.'''

        # --- SAVE TO DB ---- #

        self.balance.insert_one(funds)

        for position in positions:
            self.position.insert_one(position)

        for trade in orderbook:
            self.order_book.insert_one(trade)

        # --- SAVE TO DB ---- #

        self.logger('Websocket Closed')

if __name__ == '__main__':
    Main()
