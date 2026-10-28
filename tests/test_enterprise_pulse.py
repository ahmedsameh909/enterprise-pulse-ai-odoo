from odoo.tests import TransactionCase


class TestEnterprisePulseCompany(TransactionCase):
    def test_company_source_dataset_fields(self):
        company = self.env.company
        dataset = self.env['enterprisepulse.source.dataset'].create({
            'name': 'CRM import',
            'description': 'Imported CRM company records',
        })

        company.write({
            'description': 'Company profile',
            'source_dataset_id': dataset.id,
            'source_record_id': 'company-42',
        })

        self.assertEqual(company.description, 'Company profile')
        self.assertEqual(company.source_dataset_id, dataset)
        self.assertEqual(company.source_record_id, 'company-42')
        self.assertTrue(company.create_date)
        self.assertTrue(company.write_date)

    def test_partner_source_dataset_fields(self):
        dataset = self.env['enterprisepulse.source.dataset'].create({
            'name': 'Partner import',
        })
        partner = self.env['res.partner'].create({
            'name': 'Imported Partner',
            'source_dataset_id': dataset.id,
            'source_record_id': 'partner-42',
        })

        self.assertEqual(partner.source_dataset_id, dataset)
        self.assertEqual(partner.source_record_id, 'partner-42')

    def test_product_and_sales_source_dataset_fields(self):
        dataset = self.env['enterprisepulse.source.dataset'].create({
            'name': 'Sales import',
        })
        product = self.env['product.template'].create({
            'name': 'Imported Product',
            'source_dataset_id': dataset.id,
            'source_record_id': 'product-42',
        })
        order = self.env['sale.order'].create({
            'partner_id': self.env['res.partner'].create({
                'name': 'Imported Customer',
            }).id,
            'source_dataset_id': dataset.id,
            'source_record_id': 'order-42',
        })

        self.assertEqual(product.source_dataset_id, dataset)
        self.assertEqual(product.source_record_id, 'product-42')
        self.assertEqual(order.source_dataset_id, dataset)
        self.assertEqual(order.source_record_id, 'order-42')