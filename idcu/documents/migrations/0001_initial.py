# Generated by Django 5.0.4 on 2024-06-01 16:36

import django.db.models.deletion
import documents.lib.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('start_location', models.CharField(max_length=55)),
                ('end_location', models.CharField(max_length=55)),
                ('transportation_type', models.CharField(choices=[('TENT', 'TENT'), ('FLAT_BED', 'FLAT BED'), ('REEFER', 'REEFER')], max_length=10)),
                ('container_type', models.CharField(choices=[('ISOTHERM', documents.lib.enum.ReeferContainer['ISOTHERM']), ('MINUS_TWENTYFIVE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTYFIVE_DEGREES']), ('MINUS_TWENTYFOUR_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTYFOUR_DEGREES']), ('MINUS_TWENTYTHREE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTYTHREE_DEGREES']), ('MINUS_TWENTYTWO_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTYTWO_DEGREES']), ('MINUS_TWENTYONE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTYONE_DEGREES']), ('MINUS_TWENTY_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWENTY_DEGREES']), ('MINUS_NINETEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_NINETEEN_DEGREES']), ('MINUS_EIGHTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_EIGHTEEN_DEGREES']), ('MINUS_SEVENTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_SEVENTEEN_DEGREES']), ('MINUS_SIXTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_SIXTEEN_DEGREES']), ('MINUS_FIFTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_FIFTEEN_DEGREES']), ('MINUS_FOURTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_FOURTEEN_DEGREES']), ('MINUS_THIRTEEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_THIRTEEN_DEGREES']), ('MINUS_TWELVE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWELVE_DEGREES']), ('MINUS_ELEVEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_ELEVEN_DEGREES']), ('MINUS_TEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TEN_DEGREES']), ('MINUS_NINE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_NINE_DEGREES']), ('MINUS_EIGHT_DEGREES', documents.lib.enum.ReeferContainer['MINUS_EIGHT_DEGREES']), ('MINUS_SEVEN_DEGREES', documents.lib.enum.ReeferContainer['MINUS_SEVEN_DEGREES']), ('MINUS_SIX_DEGREES', documents.lib.enum.ReeferContainer['MINUS_SIX_DEGREES']), ('MINUS_FIVE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_FIVE_DEGREES']), ('MINUS_FOUR_DEGREES', documents.lib.enum.ReeferContainer['MINUS_FOUR_DEGREES']), ('MINUS_THREE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_THREE_DEGREES']), ('MINUS_TWO_DEGREES', documents.lib.enum.ReeferContainer['MINUS_TWO_DEGREES']), ('MINUS_ONE_DEGREES', documents.lib.enum.ReeferContainer['MINUS_ONE_DEGREES']), ('ZERO_DEGREES', documents.lib.enum.ReeferContainer['ZERO_DEGREES']), ('ONE_DEGREE', documents.lib.enum.ReeferContainer['ONE_DEGREE']), ('TWO_DEGREES', documents.lib.enum.ReeferContainer['TWO_DEGREES']), ('THREE_DEGREES', documents.lib.enum.ReeferContainer['THREE_DEGREES']), ('FOUR_DEGREES', documents.lib.enum.ReeferContainer['FOUR_DEGREES']), ('FIVE_DEGREES', documents.lib.enum.ReeferContainer['FIVE_DEGREES']), ('SIX_DEGREES', documents.lib.enum.ReeferContainer['SIX_DEGREES']), ('SEVEN_DEGREES', documents.lib.enum.ReeferContainer['SEVEN_DEGREES']), ('EIGHT_DEGREES', documents.lib.enum.ReeferContainer['EIGHT_DEGREES']), ('NINE_DEGREES', documents.lib.enum.ReeferContainer['NINE_DEGREES']), ('TEN_DEGREES', documents.lib.enum.ReeferContainer['TEN_DEGREES']), ('ELEVEN_DEGREES', documents.lib.enum.ReeferContainer['ELEVEN_DEGREES']), ('TWELVE_DEGREES', documents.lib.enum.ReeferContainer['TWELVE_DEGREES']), ('THIRTEEN_DEGREES', documents.lib.enum.ReeferContainer['THIRTEEN_DEGREES']), ('FOURTEEN_DEGREES', documents.lib.enum.ReeferContainer['FOURTEEN_DEGREES']), ('FIFTEEN_DEGREES', documents.lib.enum.ReeferContainer['FIFTEEN_DEGREES']), ('SIXTEEN_DEGREES', documents.lib.enum.ReeferContainer['SIXTEEN_DEGREES']), ('SEVENTEEN_DEGREES', documents.lib.enum.ReeferContainer['SEVENTEEN_DEGREES']), ('EIGHTEEN_DEGREES', documents.lib.enum.ReeferContainer['EIGHTEEN_DEGREES']), ('NINETEEN_DEGREES', documents.lib.enum.ReeferContainer['NINETEEN_DEGREES']), ('TWENTY_DEGREES', documents.lib.enum.ReeferContainer['TWENTY_DEGREES']), ('TWENTYONE_DEGREES', documents.lib.enum.ReeferContainer['TWENTYONE_DEGREES']), ('TWENTYTWO_DEGREES', documents.lib.enum.ReeferContainer['TWENTYTWO_DEGREES']), ('TWENTYTHREE_DEGREES', documents.lib.enum.ReeferContainer['TWENTYTHREE_DEGREES']), ('TWENTYFOUR_DEGREES', documents.lib.enum.ReeferContainer['TWENTYFOUR_DEGREES']), ('TWENTYFIVE_DEGREES', documents.lib.enum.ReeferContainer['TWENTYFIVE_DEGREES']), ('STANDARD', documents.lib.enum.TentContainer['STANDARD']), ('MEGA', documents.lib.enum.TentContainer['MEGA']), ('CAR_TRAIN', documents.lib.enum.TentContainer['CAR_TRAIN']), ('DRY_CONTAINER', documents.lib.enum.FlatBedContainer['DRY_CONTAINER']), ('REEFER_CONTAINER_WITH_GENSET', documents.lib.enum.FlatBedContainer['REEFER_CONTAINER_WITH_GENSET']), ('REEFER_CONTAINER_WITHOUT_GENSET', documents.lib.enum.FlatBedContainer['REEFER_CONTAINER_WITHOUT_GENSET'])], max_length=55)),
                ('loading_type', models.CharField(choices=[('REAR_LOAD', 'REAR LOAD'), ('TOP_LOAD', 'TOP LOAD'), ('SIDE_LOAD', 'SIDE LOAD'), ('FREE_LOAD', 'FREE LOAD')], help_text='This option can only set to Tent transport type.', max_length=55, null=True)),
                ('cargo_type', models.CharField(choices=[('FURNITURE_AND_ACCESSORIES', 'FURNITURE AND ACCESSORIES'), ('BATHROOM_EQUIPMENT_AND_ACCESSORIES', 'BATHROOM EQUIPMENT AND ACCESSORIES'), ('VEHICLE_LIGHT_SYSTEMS', 'VEHICLE LIGHT SYSTEMS'), ('AUTO_FLUIDS', 'AUTO FLUIDS'), ('AUTO_SPARE_PARTS', 'AUTO SPARE PARTS'), ('AUTO_PARTS', 'AUTO PARTS'), ('ALCOHOLIC_BEVERAGES', 'ALCOHOLIC BEVERAGES'), ('NON_ALCOHOLIC_BEVERAGES', 'NON-ALCOHOLIC BEVERAGES'), ('NON_ALCOHOLIC_BEVERAGES_JUICES_COMPOTES', 'NON-ALCOHOLIC BEVERAGES (JUICES, COMPOTES)'), ('MATCHES_AND_COMMON_HOUSEHOLD_ITEMS', 'MATCHES AND COMMON HOUSEHOLD ITEMS'), ('AUDIO_SYSTEMS', 'AUDIO SYSTEMS'), ('CHILDREN_NUTRITION', "CHILDREN'S NUTRITION"), ('CHILDREN_HYGIENE', "CHILDREN'S HYGIENE"), ('PRINTING_MATERIALS', 'PRINTING MATERIALS'), ('VEGETABLES', 'VEGETABLES'), ('CEREAL', 'CEREAL'), ('HVAC_SUPPLIES', 'HVAC SUPPLIES'), ('OUTDOOR_FURNITURE', 'OUTDOOR FURNITURE'), ('LANDSCAPE_LIGHTING', 'LANDSCAPE LIGHTING'), ('LANDSCAPE_INVENTORY', 'LANDSCAPE INVENTORY'), ('ELECTRICAL_WIRING', 'ELECTRICAL WIRING'), ('LABELS', 'LABELS'), ('VITAMINS_AND_SUPPLEMENTS', 'VITAMINS AND SUPPLEMENTS'), ('GENERAL_PRODUCTION_SUPPLIES', 'GENERAL PRODUCTION SUPPLIES'), ('PERSONAL_CARE_PRODUCTS', 'PERSONAL CARE PRODUCTS'), ('FISH', 'FISH'), ('INDUSTRIAL_LIGHTING_SYSTEMS', 'INDUSTRIAL LIGHTING SYSTEMS'), ('INDUSTRIAL_KITCHEN_EQUIPMENTS', 'INDUSTRIAL KITCHEN EQUIPMENTS'), ('BUTTER', 'BUTTER'), ('CERAMIC_TILES_AND_MATERIALS', 'CERAMIC TILES AND MATERIALS'), ('EGGS', 'EGGS'), ('COMPUTER_EQUIPMENT', 'COMPUTER EQUIPMENT'), ('COMPUTER_PERIPHERALS_AND_ACCESSORIES', 'COMPUTER PERIPHERALS & ACCESSORIES'), ('CANNED_FOODS', 'CANNED FOODS'), ('BEER', 'BEER'), ('RECYCLE_PAPER', 'RECYCLE PAPER'), ('GRAIN', 'GRAIN'), ('MEDICINE', 'MEDICINE'), ('METAL_BOTTLES', 'METAL BOTTLES'), ('METAL_PRODUCTION_MATERIALS', 'METAL PRODUCTION MATERIALS'), ('GLASS_BOTTLES', 'GLASS BOTTLES'), ('MOBILE_PHONES', 'MOBILE PHONES'), ('MOBILE_PHONES_ACCESSORIES', 'MOBILE PHONES ACCESSORIES'), ('MOTORCYCLE_PARTS', 'MOTORCYCLE PARTS'), ('PLANTS', 'PLANTS'), ('PLANTS_CARE', 'PLANTS CARE'), ('PLASTIC_BOTTLES', 'PLASTIC BOTTLES'), ('CHILDREN_INVENTORY', "CHILDREN'S INVENTORY"), ('TIRES', 'TIRES'), ('EXERCISING_ACCESSORIES', 'EXERCISING ACCESSORIES'), ('TOYS', 'TOYS'), ('STATIONERY', 'STATIONERY'), ('COOKING_OIL', 'COOKING OIL'), ('FOOD_PRODUCTS', 'FOOD PRODUCTS'), ('FOOD_PRODUCTS_SWEETS', 'FOOD PRODUCTS (SWEETS)'), ('FOOD_MANUFACTURING_MATERIALS', 'FOOD MANUFACTURING MATERIALS'), ('MEDICAL_SUPPLIES_AND_MATERIALS', 'MEDICAL SUPPLIES AND MATERIALS'), ('MEDICAL_EQUIPMENT', 'MEDICAL EQUIPMENT'), ('KITCHEN_APPLIANCES', 'KITCHEN APPLIANCES'), ('CONSTRUCTION_TOOLS_AND_EQUIPMENT', 'CONSTRUCTION TOOLS AND EQUIPMENT'), ('CONSTRUCTION_SUPPLIES', 'CONSTRUCTION SUPPLIES'), ('CONSTRUCTION_CONSUMABLES', 'CONSTRUCTION CONSUMABLES'), ('OFFICE_EQUIPMENT', 'OFFICE EQUIPMENT'), ('HOUSEHOLD_LIGHTING_SYSTEMS', 'HOUSEHOLD LIGHTING SYSTEMS'), ('HOUSEHOLD_MEDICAL_EQUIPMENT', 'HOUSEHOLD MEDICAL EQUIPMENT'), ('HOUSEHOLD_APPLIANCES', 'HOUSEHOLD APPLIANCES'), ('HOUSEHOLD_HYGIENE', 'HOUSEHOLD HYGIENE'), ('DRAWING_TOOLS', 'DRAWING TOOLS'), ('SPORTS_ACCESSORIES', 'SPORTS ACCESSORIES'), ('PERFUME', 'PERFUME'), ('OTHER_FOOD_MATERIALS', 'OTHER FOOD MATERIALS'), ('OTHER_PAPER_PRODUCTS', 'OTHER PAPER PRODUCTS'), ('CLOTHES', 'CLOTHES'), ('ENTERTAINMENT', 'ENTERTAINMENT'), ('GYM_EQUIPMENT', 'GYM EQUIPMENT'), ('SHOES', 'SHOES'), ('PHOTOGRAPHY_EQUIPMENTS', 'PHOTOGRAPHY EQUIPMENTS'), ('FABRICS', 'FABRICS'), ('WINE', 'WINE'), ('COFFEE', 'COFFEE'), ('TEA', 'TEA'), ('PET_ACCESSORIES', 'PET ACCESSORIES'), ('PET_MEDICINES', 'PET MEDICINES'), ('PET_CARE', 'PET CARE'), ('PET_FOOD', 'PET FOOD'), ('FRUIT', 'FRUIT'), ('WOOD_MANUFACTURE_MATERIALS', 'WOOD MANUFACTURE MATERIALS'), ('MEAT_PRODUCTS', 'MEAT PRODUCTS'), ('SCRAP', 'SCRAP'), ('OTHER', 'OTHER')], max_length=55)),
                ('cargo_category', models.CharField(choices=[('STANDARD', 'STANDARD'), ('NEEDS_A_REFRIGERATED_CONTAINER', 'NEEDS A REFRIGERATED CONTAINER'), ('OVERSIZE', 'OVERSIZE'), ('SPECIAL_EQUIPMENT_AND_CONSTRUCTIONS', 'SPECIAL EQUIPMENT AND CONSTRUCTIONS'), ('DANGEROUS_CATEGORY_ADR1', 'DANGEROUS CATEGORY ADR1'), ('DANGEROUS_CATEGORY_ADR2', 'DANGEROUS CATEGORY ADR2'), ('DANGEROUS_CATEGORY_ADR3', 'DANGEROUS CATEGORY ADR3'), ('DANGEROUS_CATEGORY_ADR4', 'DANGEROUS CATEGORY ADR4'), ('DANGEROUS_CATEGORY_ADR5', 'DANGEROUS CATEGORY ADR5'), ('DANGEROUS_CATEGORY_ADR6', 'DANGEROUS CATEGORY ADR6'), ('DANGEROUS_CATEGORY_ADR7', 'DANGEROUS CATEGORY ADR7'), ('DANGEROUS_CATEGORY_ADR8', 'DANGEROUS CATEGORY ADR8'), ('DANGEROUS_CATEGORY_ADR9', 'DANGEROUS CATEGORY ADR9')], max_length=55)),
                ('cargo_name', models.CharField(max_length=55)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=19)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('currency', models.CharField(choices=[('AMD', 'AMD'), ('AUD', 'AUD'), ('AZN', 'AZN'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CNY', 'CNY'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('JPY', 'JPY'), ('NZD', 'NZD'), ('SEK', 'SEK'), ('USD', 'USD')], max_length=55)),
                ('dimension', models.CharField(max_length=55)),
                ('insurance', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'IN PROGRESS'), ('FINISHED', 'FINISHED')], max_length=25)),
                ('carrier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrier_orders', to='companies.company')),
                ('forwarder', models.ForeignKey(help_text='The owner of this order.', on_delete=django.db.models.deletion.CASCADE, related_name='forwarder_orders', to='companies.company')),
                ('shipper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipper_orders', to='companies.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('file', models.FileField(upload_to='order_files/')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
