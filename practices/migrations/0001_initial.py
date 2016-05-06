# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'practices_subject', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'practices', ['Subject'])

        # Adding model 'Field'
        db.create_table(u'practices_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Subject'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'practices', ['Field'])

        # Adding model 'Axis'
        db.create_table(u'practices_axis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Subject'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'practices', ['Axis'])

        # Adding model 'AxisValue'
        db.create_table(u'practices_axisvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('axis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Axis'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'practices', ['AxisValue'])

        # Adding model 'Practice'
        db.create_table(u'practices_practice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Subject'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'practices', ['Practice'])

        # Adding model 'PracticeFieldValue'
        db.create_table(u'practices_practicefieldvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Field'])),
            ('value', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'practices', ['PracticeFieldValue'])

        # Adding unique constraint on 'PracticeFieldValue', fields ['practice', 'field']
        db.create_unique(u'practices_practicefieldvalue', ['practice_id', 'field_id'])

        # Adding model 'PracticeAxisValue'
        db.create_table(u'practices_practiceaxisvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'])),
            ('axis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Axis'])),
            ('value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.AxisValue'])),
        ))
        db.send_create_signal(u'practices', ['PracticeAxisValue'])

        # Adding unique constraint on 'PracticeAxisValue', fields ['practice', 'axis']
        db.create_unique(u'practices_practiceaxisvalue', ['practice_id', 'axis_id'])

        # Adding model 'Comment'
        db.create_table(u'practices_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'])),
        ))
        db.send_create_signal(u'practices', ['Comment'])


    def backwards(self, orm):
        # Removing unique constraint on 'PracticeAxisValue', fields ['practice', 'axis']
        db.delete_unique(u'practices_practiceaxisvalue', ['practice_id', 'axis_id'])

        # Removing unique constraint on 'PracticeFieldValue', fields ['practice', 'field']
        db.delete_unique(u'practices_practicefieldvalue', ['practice_id', 'field_id'])

        # Deleting model 'Subject'
        db.delete_table(u'practices_subject')

        # Deleting model 'Field'
        db.delete_table(u'practices_field')

        # Deleting model 'Axis'
        db.delete_table(u'practices_axis')

        # Deleting model 'AxisValue'
        db.delete_table(u'practices_axisvalue')

        # Deleting model 'Practice'
        db.delete_table(u'practices_practice')

        # Deleting model 'PracticeFieldValue'
        db.delete_table(u'practices_practicefieldvalue')

        # Deleting model 'PracticeAxisValue'
        db.delete_table(u'practices_practiceaxisvalue')

        # Deleting model 'Comment'
        db.delete_table(u'practices_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'practices.axis': {
            'Meta': {'object_name': 'Axis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Subject']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'practices.axisvalue': {
            'Meta': {'object_name': 'AxisValue'},
            'axis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Axis']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'practices.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'practices.field': {
            'Meta': {'object_name': 'Field'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Subject']"})
        },
        u'practices.practice': {
            'Meta': {'object_name': 'Practice'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Subject']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'practices.practiceaxisvalue': {
            'Meta': {'unique_together': "(('practice', 'axis'),)", 'object_name': 'PracticeAxisValue'},
            'axis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Axis']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']"}),
            'value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.AxisValue']"})
        },
        u'practices.practicefieldvalue': {
            'Meta': {'unique_together': "(('practice', 'field'),)", 'object_name': 'PracticeFieldValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Field']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']"}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'practices.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['practices']