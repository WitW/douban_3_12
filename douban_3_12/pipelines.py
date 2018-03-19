# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class Douban312Pipeline(object):
    def process_item(self, item, spider):
        movie_name = item.get("movie_name")[0]
        movie_type = item.get("movie_type")[0]
        rating_num = item.get("rating_num")[0]
        watch_num = item.get("watch_num")[0]

        db = pymysql.connect(host='localhost',port=3307,user='dlh',passwd="123456",db="MOVIE",charset="utf8mb4")
        cursor = db.cursor()

        sql = 'insert into movie(movie_name,movie_type,rating_num,watch_num) values(%s,%s,%s,%s)'

        cursor.execute(sql,(movie_name,movie_type,rating_num,watch_num))
        db.commit()
        db.close()