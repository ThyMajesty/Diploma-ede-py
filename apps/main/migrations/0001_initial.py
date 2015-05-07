# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table('main_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('exp', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('main', ['Level'])

        # Adding model 'Achivment'
        db.create_table('main_achivment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('main', ['Achivment'])

        # Adding model 'UserExt'
        db.create_table('main_userext', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ue_u', to=orm['auth.User'])),
            ('current_level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('current_exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
        ))
        db.send_create_signal('main', ['UserExt'])

        # Adding M2M table for field achivment_list on 'UserExt'
        m2m_table_name = db.shorten_name('main_userext_achivment_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userext', models.ForeignKey(orm['main.userext'], null=False)),
            ('achivment', models.ForeignKey(orm['main.achivment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userext_id', 'achivment_id'])

        # Adding model 'Category'
        db.create_table('main_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('main', ['Category'])

        # Adding model 'CategoryUserLevel'
        db.create_table('main_categoryuserlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cul_u', to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cul_c', to=orm['main.Category'])),
            ('current_level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('current_exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main', ['CategoryUserLevel'])

        # Adding model 'TaskType'
        db.create_table('main_tasktype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tt_u', to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tt_c', to=orm['main.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('color', self.gf('django.db.models.fields.CharField')(default='ff0000', max_length=255)),
        ))
        db.send_create_signal('main', ['TaskType'])

        # Adding model 'Comment'
        db.create_table('main_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='c_t', to=orm['main.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
        ))
        db.send_create_signal('main', ['Comment'])

        # Adding model 'Progress'
        db.create_table('main_progress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='p_t', to=orm['main.Task'])),
            ('percent', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('message', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('main', ['Progress'])

        # Adding model 'ProgressImage'
        db.create_table('main_progressimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('progress', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pi_p', to=orm['main.Progress'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
        ))
        db.send_create_signal('main', ['ProgressImage'])

        # Adding model 'TaskImage'
        db.create_table('main_taskimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ti_t', to=orm['main.Task'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
        ))
        db.send_create_signal('main', ['TaskImage'])

        # Adding model 'Task'
        db.create_table('main_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_create', self.gf('django.db.models.fields.related.ForeignKey')(related_name='t_uc', to=orm['auth.User'])),
            ('task_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='t_tt', to=orm['main.TaskType'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='t_c', to=orm['main.Category'])),
            ('member_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('text_content', self.gf('django.db.models.fields.TextField')()),
            ('video_link', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('members_min', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('members_max', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cost_need', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cost_now', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('min_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_start', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_finish', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('geojson', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table('main_level')

        # Deleting model 'Achivment'
        db.delete_table('main_achivment')

        # Deleting model 'UserExt'
        db.delete_table('main_userext')

        # Removing M2M table for field achivment_list on 'UserExt'
        db.delete_table(db.shorten_name('main_userext_achivment_list'))

        # Deleting model 'Category'
        db.delete_table('main_category')

        # Deleting model 'CategoryUserLevel'
        db.delete_table('main_categoryuserlevel')

        # Deleting model 'TaskType'
        db.delete_table('main_tasktype')

        # Deleting model 'Comment'
        db.delete_table('main_comment')

        # Deleting model 'Progress'
        db.delete_table('main_progress')

        # Deleting model 'ProgressImage'
        db.delete_table('main_progressimage')

        # Deleting model 'TaskImage'
        db.delete_table('main_taskimage')

        # Deleting model 'Task'
        db.delete_table('main_task')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.achivment': {
            'Meta': {'object_name': 'Achivment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'main.categoryuserlevel': {
            'Meta': {'object_name': 'CategoryUserLevel'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cul_c'", 'to': "orm['main.Category']"}),
            'current_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'current_level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cul_u'", 'to': "orm['auth.User']"})
        },
        'main.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'c_t'", 'to': "orm['main.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'main.level': {
            'Meta': {'object_name': 'Level'},
            'exp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'main.progress': {
            'Meta': {'object_name': 'Progress'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'percent': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'p_t'", 'to': "orm['main.Task']"})
        },
        'main.progressimage': {
            'Meta': {'object_name': 'ProgressImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'progress': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pi_p'", 'to': "orm['main.Progress']"})
        },
        'main.task': {
            'Meta': {'object_name': 'Task'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'t_c'", 'to': "orm['main.Category']"}),
            'cost_need': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cost_now': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_finish': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'geojson': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'members_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'members_min': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'min_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'t_tt'", 'to': "orm['main.TaskType']"}),
            'text_content': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'user_create': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'t_uc'", 'to': "orm['auth.User']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'main.taskimage': {
            'Meta': {'object_name': 'TaskImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ti_t'", 'to': "orm['main.Task']"})
        },
        'main.tasktype': {
            'Meta': {'object_name': 'TaskType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_c'", 'to': "orm['main.Category']"}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'ff0000'", 'max_length': '255'}),
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tt_u'", 'to': "orm['auth.User']"})
        },
        'main.userext': {
            'Meta': {'object_name': 'UserExt'},
            'achivment_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'u_a'", 'symmetrical': 'False', 'to': "orm['main.Achivment']"}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'current_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'current_level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ue_u'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['main']