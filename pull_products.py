from lxml import etree
from requests import request
from lxml import html
import requests
import os
import random

def urls_data():
	url_data = ['/mizrakli-panel-cit/',
		'/laleli-panel-cit/',
		'/yarasa-panel-cit/',
		'/yeni-urunler/',
		'/pirana-panel-cit/',
		'/ferforje-demir-korkuluk/']
	return url_data

def get_root_folder():
	return 'product'

def get_html_data(url):
	res = request('GET', url)
	html_data = html.fromstring(res.content)
	return html_data

def get_title_in_data(html_data):
	title = html_data.xpath('//h1')[1]
	export_title = (etree.tostring(title, pretty_print=True))
	return export_title

def get_table_in_data(html_data):
	table = html_data.xpath('//table[@class="table table-responsive"]')[0]
	export_table = (etree.tostring(table, pretty_print=True))
	return export_table

def get_description_in_data(html_data):
	description = html_data.xpath('//div[@class="col-md-12"]//p')
	return_data = []
	for item in description:
		export_description = (etree.tostring(item, pretty_print=True))
		return_data.append(export_description)
	return return_data

def get_single_image_in_data(html_data):
	image_url  = res.xpath('//div[@class="thumbnail"]//img//@data-lazy-src')[0]
	return image_url

def download_image(file_path, url):
	root_folder = get_root_folder()
	f = open("{}/{}/01.jpg".format(root_folder, file_path), 'wb')
	f.write(requests.get(url).content)
	f.close()


def create_folder(folder_name):
	root_folder = get_root_folder()
    os.mkdir('{}/{}'.format(root_folder, folder_name))

def create_txt(root, data, header):
	root_folder = get_root_folder()
	text_file = open("{}/{}/{}.txt".format(root_folder, root, header), "w")
	str_data = str(data)
	text_file.write(str_data)
	text_file.close()


def start_migrate():
	data = urls_data()
	for url in data:
		try:
			html_data = get_html_data(url)
			title = get_title_in_data(html_data).replace('<h1>', '').replace('</h1>', '')
			folder_root = random.random()
			create_folder(folder_root)
			table = get_table_in_data(html_data)
			create_txt(root=folder_root, data=table, header='table')
			description = get_description_in_data(html_data)
			create_txt(root=folder_root, data=description, header='description')
			image_url = get_single_image_in_data(html_data)
			download_image(file_path=folder_root, url=image_url)
		except:
			continue


