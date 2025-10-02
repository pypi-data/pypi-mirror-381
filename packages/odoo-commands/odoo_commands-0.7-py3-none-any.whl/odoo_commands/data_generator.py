import base64
import functools
import inspect

from cryptography.utils import cached_property
from passlib.utils import classproperty
from psutil import users

from odoo_commands.utils import create_env


def populate_command(database: str, populate_script):
    import runpy

    global_vars = runpy.run_path(
        populate_script,
        init_globals={'DataGenerator': DataGenerator},
    )
    DatabaseGenerator = global_vars['DatabaseGenerator']
    DatabaseGenerator().generate(database)


class DataGenerator:
    DEFAULT_LANG = 'en_US'
    DEFAULT_USER_PASSWORD = '123'

    lang = DEFAULT_LANG

    env_context = {
        # 'lang': lang,
    }

    populate_params = {
        'main_company': 'base.main_company',

        'usa': 'base.us',
        'russia': 'base.ru',
        'ruble': 'base.RUB',

        'russian': 'base.lang_ru',
        'admin': 'base.user_admin',

        'route_kitting': 'stock_kitting_rule.route_kitting',
        'route_mto_mts': 'stock_mts_mto_rule.route_mto_mts',
        'route_manufacture': 'mrp.route_warehouse0_manufacture',
        'route_mto': 'stock.route_warehouse0_mto',

        'route_supply': 'mrp_ext.route_supply',
        'ru_account_chart_template': 'l10n_ru.l10n_ru_account_chart_template',

        'nds_tax_group': 'sintez_l10n_ru.tax_group_nds',

        # stock
        'location_customers': 'stock.stock_location_customers',
        'location_suppliers': 'stock.stock_location_suppliers',

        # UoM
        'unit': 'uom.product_uom_unit',
        'kg': 'uom.product_uom_kgm',

        # product
        'pricelist': 'product.list0',
        'product_category_all': 'product.product_category_all',

        'treasure_department_tag': 'l10n_ru_state_org.partner_category_treasure_department',

        'account_type_expenses': 'account.data_account_type_expenses',
    }

    # @cached_property
    # def lang(self):
    #     if self._lang is not None:
    #         return self._lang
    #
    # @lang.setter
    # def lang(self, lang_code):
    #     # lang = self.env['res.lang'].with_context(active_test=False).search(['code', '=', lang_code])
    #     lang = self.env.ref(f'base.lang_{lang_code}')
    #     if not lang.active:
    #         lang.action_unarchive()
    #     if self._lang != lang.code:
    #         context = dict(self.env.context, lang=lang.code)
    #         self.env = self.env(context=context)
    #     self._lang = lang.code
    #
    # def set_currency(self, code):
    #     # currency = self.env['res.currency'].with_context(active_test=False).search(['name', '=', code])
    #     currency = self.env.ref(f'base.{code.upper()}')
    #     # currency.ensure_one()
    #     if not currency.active:
    #         currency.action_unarchive()
    #     self.currency = currency

    # @classproperty
    # def attribute_record_xml_ids(cls):
    #     xml_ids = {}
    #     for klass in reversed(cls.__mro__):
    #         xml = getattr(klass, 'xml', None)
    #         if xml:
    #             xml_ids.update(xml)
    #     return xml_ids

    def account(self, env, company, code):
        return env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', '=', code),
        ]).ensure_one()

    def get_account(self, env, company):
        return functools.partial(self.account, env, company)

    def create_company(self, env, vals):
        company = env['res.company'].create(vals)
        env.user.company_ids = [(4, company.id)]

    def execute_settings(self, env, company, vals):
        env['res.config.settings'].with_company(company).create(vals).execute()

    def create_property(self, env, model_name, field_name, res_id, company, value):
        field = env['ir.model.fields']._get(model_name, field_name)
        field_type = env[model_name]._fields[field_name].type

        # TODO Make res_id is list of ids
        property_vals = {
            'fields_id': field.id,
            'company_id': company.id,
            'res_id': res_id,
        }

        prop = env['ir.property'].search(
            [(name, '=', value) for name, value in property_vals.items()]
        )

        if prop:
            prop.write({
                'value': value,
                'type': field_type,
            })
        else:
            env['ir.property'].create(
                dict(property_vals, **{
                    'name': field_name,
                    'value': value,
                    'type': field_type,
                })
            )

    def create_user(self, env, vals, groups=()):
        vals.setdefault('email', vals['login'] + '@example.com')
        vals.setdefault('password', self.DEFAULT_USER_PASSWORD)

        vals.setdefault('company_ids', [(4, vals['company_id'])])

        main_company = env.ref('base.main_company')

        # TODO Fix ref
        # russia = env.ref('base.ru')
        vals.setdefault('country_id', main_company.country_id.id)
        vals.setdefault('lang', 'ru_RU')
        vals.setdefault('tz', 'Europe/Saratov')

        if not vals.get('groups_id'):
            vals['groups_id'] = [env.ref(xml_id).id for xml_id in groups]
        elif groups:
            raise ValueError

        return env['res.users'].with_context(no_reset_password=True).create(vals)

    def find_warehouse(self, env, company):
        return env['stock.warehouse'].search(
            [('company_id', '=', company.id)],
            order='id',
            limit=1,
        )

    def attach_file(self, env, record, name, datas=b'', **kwargs):
        record.ensure_one()
        assert isinstance(datas, bytes)

        return env['ir.attachment'].create(dict(kwargs, **{
            'res_model': record._name,
            'res_id': record.id,
            'name': name,
            'datas': base64.encodebytes(datas),
        }))

    # #################################################
    def get_populate_param(self, env, name):

        xml_id = self.populate_params.get(name)
        if not xml_id:
            raise LookupError

        record = env.ref(xml_id)
        if record._name in {'res.lang', 'res.currency'} and not record.active:
            record.action_unarchive()

        return record

    def activate_language(self, env, lang):
        language = env['res.lang'].with_context(active_test=False).search([('code', '=', lang)])
        if not language.active:
            language.action_unarchive()

        env.user.lang = lang
        env.ref('base.user_admin').lang = lang

    # Main
    def generate(self, database: str):
        env_context = dict(self.env_context)
        env_context.setdefault('lang', self.lang)
        env = create_env(database, context=env_context)

        if self.lang != self.DEFAULT_LANG:
            self.activate_language(env, self.lang)

        param_values = [
            self.get_populate_param(env, name)
            for name in inspect.signature(self.populate).parameters.keys()
            if name != 'env'
        ]

        records = self.populate(env, *param_values)
        # self.save_refs(records)
        env.cr.commit()

    def populate(self, env):
        raise NotImplementedError

    def save_refs(self, env, records: dict):
        import odoo

        if not records:
            return

        ModelData = env['ir.model.data']

        for name, value in records.items():
            if not isinstance(value, odoo.models.Model):
                continue

            if len(value) == 1 and not ModelData.search_count([
                ('model', '=', value._name),
                ('res_id', '=', value.id),
            ]):
                ModelData.create({
                    'module': 'test',
                    'name': name,
                    'model': value._name,
                    'res_id': value.id,
                })
