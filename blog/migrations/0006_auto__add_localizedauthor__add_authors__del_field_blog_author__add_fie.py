# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalizedAuthor'
        db.create_table('blog_localizedauthor', (
            ('localizednode_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.LocalizedNode'], unique=True, primary_key=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Authors'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('description', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['LocalizedAuthor'])

        # Adding model 'Authors'
        db.create_table('blog_authors', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('node_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['node.Node'], unique=True, primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Authors'])

        # Deleting field 'Blog.author'
        db.delete_column('blog_blog', 'author_id')

        # Adding field 'Blog.created_by'
        db.add_column('blog_blog', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Authors'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'LocalizedAuthor'
        db.delete_table('blog_localizedauthor')

        # Deleting model 'Authors'
        db.delete_table('blog_authors')

        # Adding field 'Blog.author'
        db.add_column('blog_blog', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=4, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Blog.created_by'
        db.delete_column('blog_blog', 'created_by_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'blog.authors': {
            'Meta': {'object_name': 'Authors', '_ormbases': ['node.Node', 'auth.User']},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'blog.blog': {
            'Meta': {'object_name': 'Blog', '_ormbases': ['node.Node']},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Authors']", 'null': 'True', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'blog.localizedauthor': {
            'Meta': {'object_name': 'LocalizedAuthor', '_ormbases': ['node.LocalizedNode']},
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'localizednode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['node.LocalizedNode']", 'unique': 'True', 'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Authors']"})
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