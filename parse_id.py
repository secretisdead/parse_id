import re
import uuid

from base64_url import base64_url_encode, base64_url_decode

def parse_id(id):
	if isinstance(id, bytes):
		id_bytes = id
		id = base64_url_encode(id)
	elif isinstance(id, str):
		if re.compile(r'[^a-zA-Z0-9_\-]').search(id):
			raise ValueError('String contained non-base64_url characters')
		id_bytes = base64_url_decode(id)
	else:
		raise TypeError
	return (id, id_bytes)

def get_id_bytes(id):
	if isinstance(id, bytes):
		return id
	return base64_url_decode(id)

def generate_or_parse_id(id):
	if not id:
		id_bytes = uuid.uuid4().bytes
		id = base64_url_encode(id_bytes)
	else:
		id, id_bytes = parse_id(id)
	return (id, id_bytes)
