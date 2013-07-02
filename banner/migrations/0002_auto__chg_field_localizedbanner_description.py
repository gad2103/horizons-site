# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LocalizedBanner.description'
        db.alter_column('banner_localizedbanner', 'description', self.gf('tinymce.models.HTMLField')(null=True))

    def backwards(self, orm):

        # Changing field 'LocalizedBanner.description'
        db.alter_column('banner_localizedbanner', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        'banner.banner': {
            'Meta': {'object_name': 'Banner', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banner.BannerCategory']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'banner.bannercategory': {
            'Meta': {'object_name': 'BannerCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'banner.localizedbanner': {
            'Meta': {'object_name': 'LocalizedBanner', '_ormbases': ['node.Node']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banner.Banner']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'node.datastate': {
            'Meta': {'object_name': 'DataState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'node.node': {
            'Meta': {'object_name': 'Node'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'data_state': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['node.DataState']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['banner']