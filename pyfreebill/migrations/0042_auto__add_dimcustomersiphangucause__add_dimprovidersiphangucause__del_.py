# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DimCustomerSipHangucause'
        db.create_table('dim_customer_sip_hangupcause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyfreebill.Company'])),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('sip_hangupcause', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyfreebill.DimDate'])),
            ('total_calls', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pyfreebill', ['DimCustomerSipHangucause'])

        # Adding model 'DimProviderSipHangucause'
        db.create_table('dim_provider_sip_hangupcause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyfreebill.Company'])),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('sip_hangupcause', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyfreebill.DimDate'])),
            ('total_calls', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pyfreebill', ['DimProviderSipHangucause'])

        # Deleting field 'DimCustomerHangucause.sip_hangupcause'
        db.delete_column('dim_customer_hangupcause', 'sip_hangupcause')

        # Deleting field 'DimProviderHangucause.sip_hangupcause'
        db.delete_column('dim_provider_hangupcause', 'sip_hangupcause')


    def backwards(self, orm):
        # Deleting model 'DimCustomerSipHangucause'
        db.delete_table('dim_customer_sip_hangupcause')

        # Deleting model 'DimProviderSipHangucause'
        db.delete_table('dim_provider_sip_hangupcause')

        # Adding field 'DimCustomerHangucause.sip_hangupcause'
        db.add_column('dim_customer_hangupcause', 'sip_hangupcause',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DimProviderHangucause.sip_hangupcause'
        db.add_column('dim_provider_hangupcause', 'sip_hangupcause',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'comments.comment': {
            'Meta': {'ordering': "('submit_date',)", 'object_name': 'Comment', 'db_table': "'django_comments'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_set_for_comment'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comment_comments'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pyfreebill.acllists': {
            'Meta': {'ordering': "('acl_name',)", 'object_name': 'AclLists', 'db_table': "'acl_lists'"},
            'acl_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'default_policy': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyfreebill.aclnodes': {
            'Meta': {'ordering': "('company', 'policy', 'cidr')", 'object_name': 'AclNodes', 'db_table': "'acl_nodes'"},
            'cidr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.AclLists']"}),
            'policy': ('django.db.models.fields.CharField', [], {'default': "'allow'", 'max_length': '10'})
        },
        u'pyfreebill.carriercidnormalizationrules': {
            'Meta': {'ordering': "('company',)", 'object_name': 'CarrierCIDNormalizationRules', 'db_table': "'carrier_cid_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.carriernormalizationrules': {
            'Meta': {'ordering': "('company', 'prefix')", 'object_name': 'CarrierNormalizationRules', 'db_table': "'carrier_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.cdr': {
            'Meta': {'ordering': "('start_stamp', 'customer')", 'object_name': 'CDR', 'db_table': "'cdr'"},
            'answered_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'billsec': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bleg_uuid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'chan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cost_destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer_related'", 'null': 'True', 'to': u"orm['pyfreebill.Company']"}),
            'customer_ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'effectiv_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'effective_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'end_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gateway': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.SofiaGateway']", 'null': 'True'}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'hangup_cause_q850': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hangup_disposition': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'lcr_carrier_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carrier_related'", 'null': 'True', 'to': u"orm['pyfreebill.Company']"}),
            'lcr_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']", 'null': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'ratecard_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']", 'null': 'True'}),
            'read_codec': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'sell_destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'sip_hangup_cause': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'sip_rtp_rxstat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'sip_rtp_txstat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'sip_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'start_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'switch_ipv4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'switchname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'pyfreebill.company': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Company', 'db_table': "'company'"},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'billing_cycle': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '10'}),
            'credit_limit': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'}),
            'customer_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '6'}),
            'customer_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'prepaid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'supplier_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '6'}),
            'supplier_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_number': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'pyfreebill.companybalancehistory': {
            'Meta': {'ordering': "('company', 'date_added')", 'object_name': 'CompanyBalanceHistory', 'db_table': "'company_balance_history'"},
            'amount_debited': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'amount_refund': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'customer_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation_type': ('django.db.models.fields.CharField', [], {'default': "'customer'", 'max_length': '10'}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'supplier_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'})
        },
        u'pyfreebill.customercidnormalizationrules': {
            'Meta': {'ordering': "('company',)", 'object_name': 'CustomerCIDNormalizationRules', 'db_table': "'customer_cid_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.customerdirectory': {
            'Meta': {'ordering': "('company', 'name')", 'object_name': 'CustomerDirectory', 'db_table': "'customer_directory'"},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_auth_failures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'multiple_registrations': ('django.db.models.fields.CharField', [], {'default': "'false'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'outbound_caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'outbound_caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'sip_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'})
        },
        u'pyfreebill.customernormalizationrules': {
            'Meta': {'ordering': "('company', 'prefix')", 'object_name': 'CustomerNormalizationRules', 'db_table': "'customer_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.customerratecards': {
            'Meta': {'ordering': "('company', 'priority', 'ratecard')", 'object_name': 'CustomerRateCards', 'db_table': "'customer_ratecards'"},
            'allow_negative_margin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'ratecard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']"}),
            'tech_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7', 'null': 'True', 'blank': 'True'})
        },
        u'pyfreebill.customerrates': {
            'Meta': {'ordering': "('ratecard', 'prefix', 'enabled')", 'unique_together': "(('ratecard', 'prefix'),)", 'object_name': 'CustomerRates', 'db_table': "'customer_rates'"},
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '5'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '5'}),
            'ratecard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']"})
        },
        u'pyfreebill.destinationnumberrules': {
            'Meta': {'ordering': "('prefix',)", 'object_name': 'DestinationNumberRules', 'db_table': "'destination_norm_rules'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'format_num': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'pyfreebill.dimcustomerdestination': {
            'Meta': {'ordering': "('date', 'customer', 'destination')", 'object_name': 'DimCustomerDestination', 'db_table': "'dim_customer_destination'"},
            'avg_duration': ('django.db.models.fields.IntegerField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration': ('django.db.models.fields.IntegerField', [], {}),
            'min_duration': ('django.db.models.fields.IntegerField', [], {}),
            'success_calls': ('django.db.models.fields.IntegerField', [], {}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_duration': ('django.db.models.fields.IntegerField', [], {}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'pyfreebill.dimcustomerhangucause': {
            'Meta': {'ordering': "('date', 'customer', 'hangupcause')", 'object_name': 'DimCustomerHangucause', 'db_table': "'dim_customer_hangupcause'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimcustomersiphangucause': {
            'Meta': {'ordering': "('date', 'customer', 'sip_hangupcause')", 'object_name': 'DimCustomerSipHangucause', 'db_table': "'dim_customer_sip_hangupcause'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sip_hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimdate': {
            'Meta': {'ordering': "('date',)", 'object_name': 'DimDate', 'db_table': "'date_dimension'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'day_of_week': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hour': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'pyfreebill.dimproviderdestination': {
            'Meta': {'ordering': "('date', 'provider', 'destination')", 'object_name': 'DimProviderDestination', 'db_table': "'dim_provider_destination'"},
            'avg_duration': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration': ('django.db.models.fields.IntegerField', [], {}),
            'min_duration': ('django.db.models.fields.IntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'success_calls': ('django.db.models.fields.IntegerField', [], {}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_duration': ('django.db.models.fields.IntegerField', [], {}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'pyfreebill.dimproviderhangucause': {
            'Meta': {'ordering': "('date', 'provider', 'hangupcause')", 'object_name': 'DimProviderHangucause', 'db_table': "'dim_provider_hangupcause'"},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimprovidersiphangucause': {
            'Meta': {'ordering': "('date', 'provider', 'sip_hangupcause')", 'object_name': 'DimProviderSipHangucause', 'db_table': "'dim_provider_sip_hangupcause'"},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'sip_hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.emailaddress': {
            'Meta': {'object_name': 'EmailAddress', 'db_table': "'contacts_email_addresses'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'pyfreebill.group': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Group', 'db_table': "'contacts_groups'"},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pyfreebill.Company']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pyfreebill.Person']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'pyfreebill.hangupcause': {
            'Meta': {'ordering': "('code',)", 'object_name': 'HangupCause', 'db_table': "'hangup_cause'"},
            'cause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enumeration': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyfreebill.instantmessenger': {
            'Meta': {'object_name': 'InstantMessenger', 'db_table': "'contacts_instant_messengers'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'im_account': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'default': "'jabber'", 'max_length': '11'})
        },
        u'pyfreebill.lcrgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'LCRGroup', 'db_table': "'lcr_group'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcrtype': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'pyfreebill.lcrproviders': {
            'Meta': {'object_name': 'LCRProviders', 'db_table': "'lcr_providers'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']"}),
            'provider_tariff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.ProviderTariff']"})
        },
        u'pyfreebill.person': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Person', 'db_table': "'contacts_people'"},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'pyfreebill.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber', 'db_table': "'contacts_phone_numbers'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pyfreebill.providerrates': {
            'Meta': {'ordering': "('enabled', 'provider_tariff', 'digits')", 'unique_together': "(('digits', 'provider_tariff'),)", 'object_name': 'ProviderRates', 'db_table': "'provider_rates'"},
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '5'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'digits': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '5'}),
            'provider_tariff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.ProviderTariff']"})
        },
        u'pyfreebill.providertariff': {
            'Meta': {'ordering': "('enabled', 'quality', 'reliability')", 'object_name': 'ProviderTariff', 'db_table': "'provider_tariff'"},
            'carrier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'cid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_strip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'default': "'100'", 'blank': 'True'}),
            'reliability': ('django.db.models.fields.IntegerField', [], {'default': "'100'", 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'tail_strip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.ratecard': {
            'Meta': {'ordering': "('name', 'enabled')", 'object_name': 'RateCard', 'db_table': "'ratecard'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcrgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'pyfreebill.sipprofile': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('sip_ip', 'sip_port'),)", 'object_name': 'SipProfile', 'db_table': "'sip_profile'"},
            'accept_blind_reg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auth_calls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'disable_transcoding': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ext_rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'ext_sip_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,PCMA'", 'max_length': '100'}),
            'log_auth_failures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'outbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,PCMA'", 'max_length': '100'}),
            'rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'sip_ip': ('django.db.models.fields.CharField', [], {'default': "'/32'", 'max_length': '100'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'default': "'pyfreebilling'", 'max_length': '50'})
        },
        u'pyfreebill.sofiagateway': {
            'Meta': {'ordering': "('company', 'name')", 'object_name': 'SofiaGateway', 'db_table': "'sofia_gateway'"},
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'channels': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'codec': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'expire_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600', 'null': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'from_domain': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '35', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'proxy': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'realm': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'retry_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True'}),
            'sip_cid_type': ('django.db.models.fields.CharField', [], {'default': "'rpid'", 'max_length': '10'}),
            'sip_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.SipProfile']"}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '35', 'blank': 'True'})
        },
        u'pyfreebill.specialdate': {
            'Meta': {'object_name': 'SpecialDate', 'db_table': "'contacts_special_dates'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'every_year': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'occasion': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'pyfreebill.streetaddress': {
            'Meta': {'object_name': 'StreetAddress', 'db_table': "'contacts_street_addresses'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'pyfreebill.voipswitch': {
            'Meta': {'ordering': "('name',)", 'object_name': 'VoipSwitch', 'db_table': "'voip_switch'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pyfreebill.website': {
            'Meta': {'object_name': 'WebSite', 'db_table': "'contacts_web_sites'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pyfreebill']