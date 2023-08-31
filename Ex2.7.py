# EX 2.7 Write a function convert_to_ascii to convert Vietnamese characters into ASCII ones
# Write a function convert_to_ascii to convert Vietnamese characters into ASCII ones.
#
# Test data:
#
# Input: Xin chào Việt Nam
#
# Output: Xin chao Viet Nam
import re
s = input()

def convert_to_ascii(s):
	s = re.sub(r'[àáạảãâậẩẫầăằắẳẵặ]', 'a', s)
	s = re.sub(r'[ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ]', 'A', s)
	s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
	s = re.sub(r'[ÉÈẸẺẼÊỀẾỆỂỄ]', 'E', s)
	s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
	s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O',s)
	s = re.sub(r'[ìíịỉĩ]', 'i', s)
	s = re.sub(r'[ÌÍỊỈĨ]', 'I',s)
	s = re.sub(r'[ùúụủũưừứựửữ]', 'u',s)
	s = re.sub(r'[ÙÚỤỦŨƯỪỨỰỬỮ]', 'U',s)
	s = re.sub(r'[ỳýỵỷỹ]', 'y',s)
	s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
	s = re.sub(r'[đ]', 'd',s)
	s = re.sub(r'[Đ]', 'D',s)
	print(s)
convert_to_ascii(s)


