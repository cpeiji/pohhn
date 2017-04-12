

class SqlUtil:


    @staticmethod
    def query_all_sql(table_name):
        sql = "select * from "+table_name
        return sql

    @staticmethod
    def query_by_id_sql(table_name,id):
        sql = "select * from " + table_name+" where id="+str(id)
        return sql