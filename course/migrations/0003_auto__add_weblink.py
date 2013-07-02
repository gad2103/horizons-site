# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weblink'
        db.create_table('course_weblink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('course', ['Weblink'])

        # Adding M2M table for field courses on 'Weblink'
        db.create_table('course_weblink_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('weblink', models.ForeignKey(orm['course.weblink'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('course_weblink_courses', ['weblink_id', 'course_id'])


    def backwards(self, orm):
        # Deleting model 'Weblink'
        db.delete_table('course_weblink')

        # Removing M2M table for field courses on 'Weblink'
        db.delete_table('course_weblink_courses')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.class': {
            'Meta': {'object_name': 'Class', '_ormbases': ['node.Node']},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['instructor.Instructor']", 'null': 'True', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'course.course': {
            'Meta': {'object_name': 'Course', '_ormbases': ['node.Node']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Target']"})
        },
        'course.localizedcourse': {
            'Meta': {'object_name': 'LocalizedCourse', '_ormbases': ['node.LocalizedNode']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"})
        },
        'course.localizedtarget': {
            'Meta': {'object_name': 'LocalizedTarget', '_ormbases': ['node.LocalizedNode']},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Target']"})
        },
        'course.target': {
            'Meta': {'object_name': 'Target', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.TargetCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'subname': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'})
        },
        'course.targetcategory': {
            'Meta': {'object_name': 'TargetCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'course.weblink': {
            'Meta': {'object_name': 'Weblink'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['course.Course']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'instructor.instructor': {
            'Meta': {'object_name': 'Instructor', '_ormbases': ['node.Node']},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['course.Course']", 'symmetrical': 'False'})
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
        }
    }

    complete_apps = ['course']