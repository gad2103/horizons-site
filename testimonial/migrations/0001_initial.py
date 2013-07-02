# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestimonialCategory'
        db.create_table('testimonial_testimonialcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
        ))
        db.send_create_signal('testimonial', ['TestimonialCategory'])

        # Adding model 'Testimonial'
        db.create_table('testimonial_testimonial', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.Node'], unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['testimonial.TestimonialCategory'])),
        ))
        db.send_create_signal('testimonial', ['Testimonial'])

        # Adding model 'LocalizedTestimonial'
        db.create_table('testimonial_localizedtestimonial', (
            ('localizednode_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.LocalizedNode'], unique=True, primary_key=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['testimonial.Testimonial'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=63, null=True, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal('testimonial', ['LocalizedTestimonial'])


    def backwards(self, orm):
        # Deleting model 'TestimonialCategory'
        db.delete_table('testimonial_testimonialcategory')

        # Deleting model 'Testimonial'
        db.delete_table('testimonial_testimonial')

        # Deleting model 'LocalizedTestimonial'
        db.delete_table('testimonial_localizedtestimonial')


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
        'testimonial.localizedtestimonial': {
            'Meta': {'object_name': 'LocalizedTestimonial', '_ormbases': ['node.LocalizedNode']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testimonial.Testimonial']"})
        },
        'testimonial.testimonial': {
            'Meta': {'object_name': 'Testimonial', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testimonial.TestimonialCategory']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'testimonial.testimonialcategory': {
            'Meta': {'object_name': 'TestimonialCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['testimonial']