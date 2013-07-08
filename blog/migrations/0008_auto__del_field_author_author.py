# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Author.author'
        db.delete_column('blog_author', 'author_id')


    def backwards(self, orm):
        # Adding field 'Author.author'
        db.add_column('blog_author', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['auth.User'], blank=True),
                      keep_default=False)


    models = {
        'blog.author': {
            'Meta': {'object_name': 'Author', '_ormbases': ['node.Node']},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'blog.blog': {
            'Meta': {'object_name': 'Blog', '_ormbases': ['node.Node']},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Author']", 'null': 'True', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'blog.localizedauthor': {
            'Meta': {'object_name': 'LocalizedAuthor', '_ormbases': ['node.LocalizedNode']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Author']"})
        },
        'blog.localizedblog': {
            'Meta': {'object_name': 'LocalizedBlog', '_ormbases': ['node.LocalizedNode']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'exerpt': ('django.db.models.fields.CharField', [], {'max_length': '511', 'null': 'True', 'blank': 'True'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Blog']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '63'})
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
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 6, 0, 0)', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']