# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Class.location'
        db.delete_column('course_class', 'location_id')

        # Adding M2M table for field location on 'Class'
        db.create_table('course_class_location', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['course.class'], null=False)),
            ('location', models.ForeignKey(orm['location.location'], null=False))
        ))
        db.create_unique('course_class_location', ['class_id', 'location_id'])


    def backwards(self, orm):
        # Adding field 'Class.location'
        db.add_column('course_class', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field location on 'Class'
        db.delete_table('course_class_location')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.class': {
            'Meta': {'ordering': "['start_time', 'location__priority']", 'object_name': 'Class', '_ormbases': ['node.Node']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'end_time': ('django.db.models.fields.DateField', [], {}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['location.Location']", 'null': 'True', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"}),
            'schedule': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateField', [], {})
        },
        'course.course': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Course', '_ormbases': ['node.Node']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Target']"})
        },
        'course.localizedcourse': {
            'Meta': {'object_name': 'LocalizedCourse', '_ormbases': ['node.LocalizedNode']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'})
        },
        'course.localizedtarget': {
            'Meta': {'object_name': 'LocalizedTarget', '_ormbases': ['node.LocalizedNode']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Target']"})
        },
        'course.localizedtargetcategory': {
            'Meta': {'object_name': 'LocalizedTargetCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'portal localization language'", 'to': "orm['node.Language']"}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.TargetCategory']"})
        },
        'course.target': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Target', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.TargetCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'course.targetcategory': {
            'Meta': {'ordering': "['priority']", 'object_name': 'TargetCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"})
        },
        'course.weblink': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Weblink'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['course.Course']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'location.location': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Location', '_ormbases': ['node.Node']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'1000'"})
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
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 8, 0, 0)', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['course']