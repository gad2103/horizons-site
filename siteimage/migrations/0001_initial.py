# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteImageCategory'
        db.create_table('siteimage_siteimagecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
        ))
        db.send_create_signal('siteimage', ['SiteImageCategory'])

        # Adding model 'SiteImage'
        db.create_table('siteimage_siteimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['siteimage.SiteImageCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('siteimage', ['SiteImage'])


    def backwards(self, orm):
        # Deleting model 'SiteImageCategory'
        db.delete_table('siteimage_siteimagecategory')

        # Deleting model 'SiteImage'
        db.delete_table('siteimage_siteimage')


    models = {
        'siteimage.siteimage': {
            'Meta': {'object_name': 'SiteImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['siteimage.SiteImageCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'siteimage.siteimagecategory': {
            'Meta': {'object_name': 'SiteImageCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['siteimage']