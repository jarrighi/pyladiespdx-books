# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.slug'
        db.add_column(u'books_book', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime.now, max_length=256),
                      keep_default=False)

        # Adding field 'Book.date_added'
        db.add_column(u'books_book', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.slug'
        db.delete_column(u'books_book', 'slug')

        # Deleting field 'Book.date_added'
        db.delete_column(u'books_book', 'date_added')


    models = {
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'possessor': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': 'datetime.datetime.now', 'max_length': '256'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['books']