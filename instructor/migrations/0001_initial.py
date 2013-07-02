# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instructor'
        db.create_table('instructor_instructor', (
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.Node'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('instructor', ['Instructor'])

        # Adding M2M table for field topics on 'Instructor'
        db.create_table('instructor_instructor_topics', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('instructor', models.ForeignKey(orm['instructor.instructor'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('instructor_instructor_topics', ['instructor_id', 'course_id'])

        # Adding model 'LocalizedInstructor'
        db.create_table('instructor_localizedinstructor', (
            ('localizednode_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.LocalizedNode'], unique=True, primary_key=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['instructor.Instructor'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('instructor', ['LocalizedInstructor'])


    def backwards(self, orm):
        # Deleting model 'Instructor'
        db.delete_table('instructor_instructor')

        # Removing M2M table for field topics on 'Instructor'
        db.delete_table('instructor_instructor_topics')

        # Deleting model 'LocalizedInstructor'
        db.delete_table('instructor_localizedinstructor')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.course': {
            'Meta': {'object_name': 'Course', '_ormbases': ['node.Node']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Target']"})
        },
        'course.target': {
            'Meta': {'object_name': 'Target', '_ormbases': ['node.Node']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.TargetCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'course.targetcategory': {
            'Meta': {'object_name': 'TargetCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'instructor.instructor': {
            'Meta': {'object_name': 'Instructor', '_ormbases': ['node.Node']},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['course.Course']", 'symmetrical': 'False'})
        },
        'instructor.localizedinstructor': {
            'Meta': {'object_name': 'LocalizedInstructor', '_ormbases': ['node.LocalizedNode']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['instructor.Instructor']"})
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

    complete_apps = ['instructor']