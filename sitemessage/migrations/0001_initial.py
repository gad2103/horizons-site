# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteMessage'
        db.create_table('sitemessage_sitemessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('sitemessage', ['SiteMessage'])

        # Adding model 'LocalizedSiteMessage'
        db.create_table('sitemessage_localizedsitemessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sitemessage.SiteMessage'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='site message localization language', to=orm['node.Language'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('sitemessage', ['LocalizedSiteMessage'])


    def backwards(self, orm):
        # Deleting model 'SiteMessage'
        db.delete_table('sitemessage_sitemessage')

        # Deleting model 'LocalizedSiteMessage'
        db.delete_table('sitemessage_localizedsitemessage')


    models = {
        'node.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sitemessage.localizedsitemessage': {
            'Meta': {'object_name': 'LocalizedSiteMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'site message localization language'", 'to': "orm['node.Language']"}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitemessage.SiteMessage']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sitemessage.sitemessage': {
            'Meta': {'object_name': 'SiteMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['sitemessage']