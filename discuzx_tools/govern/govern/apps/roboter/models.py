#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BbsAttachment(models.Model):
    id = models.IntegerField(_('id'), primary_key=True)
    file_name = models.CharField(_('file name'), max_length=255)
    key_name = models.CharField(
        _('key name'), max_length=80, blank=True,
        null=True)
    down_link = models.CharField(
        _('down link'), max_length=150, blank=True,
        null=True)
    md5sum = models.CharField(
        _('md5sum'), max_length=80, blank=True,
        null=True)
    plate = models.IntegerField(_('plate'), blank=True, null=True)
    status = models.IntegerField(_('status'), blank=True, null=True)
    author = models.CharField(
        _('author'), max_length=45, blank=True,
        null=True)
    create_datetime = models.DateTimeField(_('create datetime'))
    upload_datetime = models.DateTimeField(
        _('upload datetime'), blank=True,
        null=True)

    class Meta:
        managed = False
        db_table = 'bbs_attachment'
        verbose_name = _('bbs attachment')
        verbose_name_plural = _('bbs attachment list')
        permissions = (("read_only", "Can read only"),)

    def __str__(self):
        return '%s' % self.id

    def __unicode__(self):
        return '%s' % self.id


class BbsMember(models.Model):
    id = models.IntegerField(_('id'), primary_key=True)
    username = models.CharField(_('username'), max_length=45)
    password = models.CharField(_('password'), max_length=45)
    email = models.CharField(_('email'), max_length=45)
    dz_uid = models.IntegerField(_('dz uid'), blank=True, null=True)
    create_datetime = models.DateTimeField(_('create datetime'))

    class Meta:
        managed = False
        db_table = 'bbs_member'
        verbose_name = _('bbs member')
        verbose_name_plural = _('bbs member list')
        permissions = (("read_only", "Can read only"),)


class BbsSurplus(models.Model):
    id = models.IntegerField(_('id'), primary_key=True)
    fid = models.IntegerField(_('fid'), blank=True, null=True)
    path = models.CharField(_('path'), max_length=255)
    md5sum = models.CharField(
        _('md5sum'), max_length=80, blank=True, null=True)
    plate = models.IntegerField(_('plate'), blank=True, null=True)
    author = models.CharField(
        _('author'), max_length=45, blank=True, null=True)
    create_datetime = models.DateTimeField(_('create datetime'))

    class Meta:
        managed = False
        db_table = 'bbs_surplus'
        verbose_name = _('bbs surplus')
        verbose_name_plural = _('bbs surplus list')
        permissions = (("read_only", "Can read only"),)


class BbsThread(models.Model):
    id = models.IntegerField(_('id'), primary_key=True)
    thread_id = models.IntegerField(_('thread id'))
    post_id = models.IntegerField(_('post id'))
    create_datetime = models.DateTimeField(_('create datetime'))
    attachment_id = models.IntegerField(
        _('attachment id'), blank=True, null=True)
    robot_data_id = models.ForeignKey(
        BbsAttachment,
        db_column='robot_data_id',
        verbose_name=_('robot data id'),
        related_name='+',
        to_field='id',
        blank=True,
        null=True)

    class Meta:
        managed = False
        db_table = 'bbs_thread'
        verbose_name = _('bbs thread')
        verbose_name_plural = _('bbs thread list')
        permissions = (("read_only", "Can read only"),)


class BbsPost(models.Model):
    id = models.IntegerField(_('id'), primary_key=True)
    uid = models.IntegerField(_('thread id'))
    tid = models.IntegerField(_('thread id'))
    pid = models.IntegerField(_('post id'))
    fid = models.IntegerField(_('plate id'))
    create_datetime = models.DateTimeField(_('create datetime'))

    class Meta:
        managed = False
        db_table = 'bbs_post'
        verbose_name = _('bbs post')
        verbose_name_plural = _('bbs post list')
        permissions = (("read_only", "Can read only"),)


class BbsPostContent(models.Model):
    choices_status = [(0, '未启用'), (1, '已启用')]

    id = models.AutoField(_('id'), primary_key=True)
    content = models.CharField(
        _('content'), max_length=800, blank=False, null=False)
    status = models.IntegerField(
        _('status'), choices=choices_status, default=1)
    user = models.ForeignKey(
        User, verbose_name=_('user'), blank=True, null=True, default=0)
    update_datetime = models.DateTimeField(_('update datetime'), auto_now=True)
    create_datetime = models.DateTimeField(
        _('create datetime'), auto_now_add=True)

    class Meta:
        db_table = 'bbs_post_content'
        verbose_name = _('bbs post content')
        verbose_name_plural = _('bbs post content list')
        permissions = (("read_only", "Can read only"),)
