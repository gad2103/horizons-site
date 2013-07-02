# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LocalizedSiteMessage.text'
        db.alter_column('sitemessage_localizedsitemessage', 'text', self.gf('tinymce.models.HTMLField')(null=True))

    def backwards(self, orm):

        # Changing field 'LocalizedSiteMessage.text'
        db.alter_column('sitemessage_localizedsitemessage', 'text', self.gf('django.db.models.fields.CharField')(default='TBD', max_length=255))

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
            'text': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'})
        },
        'sitemessage.sitemessage': {
            'Meta': {'object_name': 'SiteMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['sitemessage']