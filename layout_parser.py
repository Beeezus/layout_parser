import xml.etree.ElementTree as ET
#lxml.etree implementation of  XPath is superior
#due to more flexibility with axes and speed


class AndroidLayoutParser():
	def __init__(self, string_data):
		self.string_data=string_data

	def _parse_xml(self):
		return {
		'sign_in': self._get_sign_in_selector(self.string_data),
		'sign_up': self._get_sign_up_selector(self.string_data),
		'image': self._get_image_selector(self.string_data),
		'settings': self._get_settings_selector(self.string_data),
		'cart': self._get_cart_selector(self.string_data),
		'home': self._get_home_selector(self.string_data),
		'notifications': self._get_notifications_selector(self.string_data),
		'ideabooks':self._get_ideabooks_selector(self.string_data),
		'profile': self._get_profile_selector(self.string_data)
		}

	def _get_sign_in_selector(self, string_data):
		path = (
			'.//android.widget.FrameLayout[@content-desc="ProfileScreen"]/'
			'android.view.ViewGroup/'
			'androidx.recyclerview.widget.RecyclerView/'
			'android.widget.LinearLayout/'
			'android.widget.LinearLayout/'
			'android.widget.TextView[2]'
		)
		sign_in_element = self._extract_selection(path, string_data)
		if sign_in_element:
			return sign_in_element

	def _get_sign_up_selector(self, string_data):
		path = (
			'.//android.widget.FrameLayout[@content-desc="ProfileScreen"]/'
			'android.view.ViewGroup/'
			'androidx.recyclerview.widget.RecyclerView/'
			'android.widget.LinearLayout/'
			'android.widget.LinearLayout/'
			'android.widget.TextView[3]'
		)
		sign_up_element = self._extract_selection(path, string_data)
		if sign_up_element:
			return sign_up_element

	def _get_image_selector(self, string_data):
		path = (
			'.//android.widget.FrameLayout[@content-desc="ProfileScreen"]/'
			'android.view.ViewGroup/'
			'androidx.recyclerview.widget.RecyclerView/'
			'android.widget.LinearLayout/'
			'android.widget.LinearLayout/'
			'android.widget.ImageView'
		)
		image_element = self._extract_selection(path, string_data)
		if image_element:
			return image_element
	
	def _get_cart_selector(self, string_data):
		path = (
			'.//android.widget.FrameLayout[@NAF="true"]/'
			'android.widget.FrameLayout/'
			'android.widget.ImageView'
		)
		cart_element = self._extract_selection(path, string_data)
		if cart_element:
			return cart_element

	def _get_settings_selector(self, string_data):
		path = './/android.widget.TextView[@content-desc="Settings"]'
		settings_element = self._extract_selection(path, string_data)
		if settings_element:
			return settings_element

	def _get_home_selector(self, string_data):
		path = './/android.widget.TextView[@text="Home"]'
		home_element = self._extract_selection(path, string_data)
		if home_element:
			return home_element

	def _get_notifications_selector(self, string_data):
		path = './/android.widget.TextView[@text="Notifications"]'
		path_element = self._extract_selection(path, string_data)
		if path_element:
			return path_element

	def _get_ideabooks_selector(self, string_data):
		path = './/android.widget.TextView[@text="Ideabooks"]'
		ideabooks_element = self._extract_selection(path, string_data)
		if ideabooks_element:
			return ideabooks_element

	def _get_profile_selector(self, string_data):
		path = './/android.widget.TextView[@text="Profile"]'
		profile_element = self._extract_selection(path, string_data)
		if profile_element:
			return profile_element

	def _extract_selection(self, path, string_data):
		xml_data = self._parse_to_xml(string_data)
		if not xml_data:
			return None
		selection_element = xml_data.findall(path)
		if not selection_element:
			return None
		string_element = ET.tostring(selection_element[0])
		return string_element.rstrip()

	def _parse_to_xml(self, string_data):
		#Not handling parsing with try catch block is intentional
		#since no other reuqirements are provided I believe it is better
		#to fail parsing at this stage
		if isinstance(string_data, str):
			return ET.fromstring(string_data)

if __name__ == '__main__':
	#data = ET.parse('string_data.pdf')
	#Parsing string from multi-page pdf files consistently requires a additional
	#time for analysis and implementation, hence spoofing string import from xml
	#for this short ticket

	data = ET.parse('xml_data.xml')
	tree = data.getroot()
	string_data = ET.tostring(tree)

	test_layout = AndroidLayoutParser(string_data)
	selectors_data = test_layout._parse_xml()
	
	assert not None in selectors_data.values(), 'values were not extracted'
	assert not False in [isinstance(x, str) for x in selectors_data.values()], 'values are not strings'
