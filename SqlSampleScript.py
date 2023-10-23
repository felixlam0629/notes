import mysql.connector
import pandas as pd
from pprint import pprint
import requests

class SqlSampleScript():
    def __init__(self):
        self.user         = "root"
        self.password     = "qwER!!2345"
        self.host         = "localhost"
        # self.database     = "sql_invoicing"
        self.database     = "binance"
        self.ssl_disabled = "True"

    # Connect to SQL db
    def connect_to_sql(self):
        user         = self.user
        password     = self.password
        host         = self.host
        database     = self.database
        ssl_disabled = self.ssl_disabled

        connection = None

        try:
            connection = mysql.connector.connect(
                user         = user,
                password     = password,
                host         = host,
                database     = database,
                ssl_disabled = ssl_disabled
            )

        except:
            print("SQL connection issue")

        # connection.commit()

        return connection

    # Query data from SQL db/ do any query such as inserting/ updating data
    def query_from_sql(self, connection, sql_query):
        cursor = connection.cursor()
        query  = sql_query
        cursor.execute(query)

        data_list = cursor.fetchall()

        cursor.close()
        connection.close()

        return data_list

    # Put data into SQL db (example with binance API)
    def put_data_into_sql(self, connection):
        cursor = connection.cursor()

        symbol    = 'BTCUSDT'
        interval  = '1m'
        url       = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
        response  = requests.get(url)
        data_list = response.json()

        for data in data_list:
            timestamp   = data[0]
            open_price  = float(data[1])
            high_price  = float(data[2])
            low_price   = float(data[3])
            close_price = float(data[4])
            volume      = float(data[5])

            # query  = "INSERT INTO kline (timestamp) VALUES (%s)"
            query  = "INSERT INTO kline (timestamp, open_price, high_price, low_price, close_price, volume) VALUES (%s, %s, %s, %s, %s, %s)"
            # values = (timestamp)
            values = (timestamp, open_price, high_price, low_price, close_price, volume)

            cursor.execute(query, values)

        cursor.close()
        connection.close()

def main():
    sql_db     = SqlSampleScript()
    connection = sql_db.connect_to_sql()

    query = """
        SELECT * from kline
    """
    d = sql_db.query_from_sql(connection, query)
    pprint(d)
    exit()
    # mainly do SQL query here
    sql_query = """
                SELECT * 
                FROM clients
    """
    # sql_query = "SELECT * FROM kline LIMIT 10" # Fetching the first 1000 rows
    # sql_query = "SELECT * FROM kline LIMIT 10" # Fetching the first 1000 rows

    data_list = sql_db.query_from_sql(connection, sql_query)
    pprint(data_list)

    df = pd.DataFrame(data_list)
    df.columns = ["client_id", "name", "address", "location", "state", "phone"]
    print(df)

if __name__ == "__main__":
    main()