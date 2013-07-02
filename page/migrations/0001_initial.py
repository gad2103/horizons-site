# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageCategory'
        db.create_table('page_pagecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
        ))
        db.send_create_signal('page', ['PageCategory'])

        # Adding model 'Page'
        db.create_table('page_page', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.Node'], unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['page.PageCategory'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=63)),
        ))
        db.send_create_signal('page', ['Page'])

        # Adding model 'LocalizedPage'
        db.create_table('page_localizedpage', (
            ('localizednode_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.LocalizedNode'], unique=True, primary_key=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['page.Page'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('page', ['LocalizedPage'])


    def backwards(self, orm):
        # Deleting model 'PageCategory'
        db.delete_table('page_pagecategory')

        # Deleting model 'Page'
        db.delete_table('page_page')

        # Deleting model 'LocalizedPage'
        db.delete_table('page_localizedpage')


    models = {
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
        'node.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'node.localizednode': {
            'Meta': {'object_name': 'LocalizedNode', '_ormbases': ['node.Node']},
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'localization language'", 'to': "orm['node.Language']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'node.node': {
            'Meta': {'object_name': 'Node'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'data_state': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['node.DataState']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {})
        },
        'page.localizedpage': {
            'Meta': {'object_name': 'LocalizedPage', '_ormbases': ['node.LocalizedNode']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'page.page': {
            'Meta': {'object_name': 'Page', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.PageCategory']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'page.pagecategory': {
            'Meta': {'object_name': 'PageCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['page']