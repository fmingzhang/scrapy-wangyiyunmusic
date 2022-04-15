# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MusicPipeline:

    def open_spider(self,spider):
      self.fp=open('tt.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
       self.fp.close()


#加载settings文件
from  scrapy.utils.project import get_project_settings
import pymysql
#安装并导入pymsql
class MysqlPipline:

    def open_spider(self,spider):

     settings=get_project_settings()
     self.host=settings['DB_HOST']
     self.port=settings['DB_PORT']
     self.user=settings['DB_USER']
     self.password=settings['DB_PASSWORD']
     self.name=settings['DB_NAME']
     self.charset=settings['DB_CHARSET']

     self.connect()


    def connect(self):
         self.conn = pymysql.connect(host=self.host,port=self.port,
                                     user=self.user,password=self.password,
                                     db=self.name,charset=self.charset
                                     )


         self.cursor=self.conn.cursor()
    def process_item(self,item,spider):
        sql='insert into songSheet(sheetName,createTime,tag,introduce,cover) values("{}","{}","{}","{}","{}")'.format(item['name'],
                                                                              item['createTime'],
                                                                              item['tag'],
                                                                              item['introduce'],
                                                                              item['cover']
                                                                              )

        self.cursor.execute(sql)
        self.conn.commit()

    def close_spider(self,spider):
         self.cursor.close()
         self.conn.close()
