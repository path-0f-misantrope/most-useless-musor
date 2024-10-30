import cianparser

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_flats(deal_type="rent_long", rooms=(1), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1000,"sort_by":"price_from_min_to_max"})

print(data[0])