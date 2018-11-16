from django.http import HttpResponse

'''验证码函数，基于python'''
'''
新建viewsUtil.py，定义函数verifycode
此段代码用到了PIL中的Image、ImageDraw、ImageFont模块，需要先安装Pillow（3.4.1）包，详细文档参考http://pillow.readthedocs.io/en/3.4.x/
Image表示画布对象
ImageDraw表示画笔对象
ImageFont表示字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”，centos7 用fc-list查看字体路径，没有的话yum -y install fontconfig
开启 session 会话，需要session的数据库，用 python manage.py migrate
'''
# def verifycode(request):
# 	#引入绘图模块
# 	from PIL import Image, ImageDraw, ImageFont
# 	#引入随机函数模块
# 	import random
# 	#定义变量，用于画面的背景色、宽、高
# 	bgcolor = (random.randrange(20, 100), random.randrange(
# 		20, 100), 255)
# 	width = 100
# 	height = 37
# 	#创建画面对象
# 	im = Image.new('RGB', (width, height), bgcolor)
# 	#创建画笔对象
# 	draw = ImageDraw.Draw(im)
# 	#调用画笔的point()函数绘制噪点
# 	for i in range(0, 100):
# 		xy = (random.randrange(0, width), random.randrange(0, height))
# 		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
# 		draw.point(xy, fill=fill)
# 	#定义验证码的备选值
# 	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
# 	#随机选取4个值作为验证码
# 	rand_str = ''
# 	for i in range(0, 4):
# 		rand_str += str1[random.randrange(0, len(str1))]
# 	#构造字体对象
# 	from django.conf import settings
# 	_FONT_PATH = settings.VERIFY_CODE_FONT_PATH # settings字体路径
# 	font = ImageFont.truetype(_FONT_PATH + 'STIX-BoldItalic.otf', 23)
# 	#构造字体颜色
# 	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
# 	#绘制4个字
# 	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
# 	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
# 	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
# 	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
# 	#释放画笔
# 	del draw
# 	#存入session，用于做进一步验证
# 	request.session['verifycode'] = rand_str
# 	#内存文件操作
# 	from io import BytesIO
# 	buf = BytesIO()
# 	#将图片保存在内存中，文件类型为png
# 	im.save(buf, format='png')
# 	#将内存中的图片数据返回给客户端，MIME类型为图片png
# 	return HttpResponse(buf.getvalue(), 'image/png')

''' 分界线，两个都是实现生成验证码的代码 '''

''' 验证码，还未检验过 '''
import base64
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings  # 导入主项目settings配置

_FONT_PATH = settings.VERIFY_CODE_FONT_PATH  # 这个是字体的存储路径，根据实际填写

# 产生随机字符（大小写字母或数字）
def rnd_char():
	return random.choice(string.ascii_letters + string.digits)

# 产生随机颜色（颜色较浅，用于产生背景干扰颜色） 实际上这个对增加自动识别的难度几乎没有任何作用
def rnd_bg_color():
	return random.randint(126, 255), random.randint(126, 255), random.randint(126, 255)

# 产生随机颜色（颜色较深，用于产生验证码字符颜色）
def rnd_ch_color():
	return random.randint(10, 66), random.randint(10, 66), random.randint(10, 66)

# 产生随机字体 字体可以自己去网上下载，尽量不要太规范的字体
def rnd_font(min_size=28, max_size=34, rnd=True):
	font_types = (_FONT_PATH + 'STIX-BoldItalic.otf', _FONT_PATH + 'STIX-BoldItalic.otf', _FONT_PATH + 'STIX-BoldItalic.otf',)
	font_type = font_types[random.randint(0, len(font_types) - 1)]
	font_size = (max_size + min_size) >> 1
	if rnd:
		font_size = random.randint(min_size, max_size)
	return ImageFont.truetype(font_type, font_size, encoding='utf-8')

# 产生验证码图片，返回产生的验证码
def create_verification(max_size=34, length=4):
	left_space, top_space = int(max_size >> 1), int(max_size >> 2)
	# print('left space: {0}, top_space: {1}'.format(left_space, top_space))
	width, height = max_size * length + left_space * 2, max_size + top_space  # 图片的大小比验证码大小稍大
	# 创建初始图片
	img = Image.new('RGB', (width, height))
	pixs = img.load()
	draw = ImageDraw.Draw(img)
	# 画背景颜色
	for i in range(width):
		for j in range(height):
			pixs[i, j] = rnd_bg_color()
	ret_code = ''
	last_right = 0
	# 画验证码 TODO: 字体小角度旋转没完成
	for i in range(length):
		code = rnd_char()
		ret_code += code
		font = rnd_font(min_size=max_size - 6, max_size=max_size, rnd=True)
		font_width, font_height = font.getsize(code)
		if i == 0:
			last_right = left_space + ((max_size - font_width) >> 1) + font_width
			draw.text((left_space + ((max_size - font_width) >> 1), top_space - random.randint(6, 12)),
					  code, fill=rnd_ch_color(), font=font)
		else:
			offset = random.randint(1, 6)
			draw.text((last_right - offset, top_space - random.randint(6, 12)), code,
					  fill=rnd_ch_color(), font=font)
			last_right += (font_width - offset)
	# 画干扰线，很难看暂时不用
	for k in range(2):
		draw.line(((0, random.randint(2, max_size - 2)), (length * max_size, random.randint(0, max_size))),
				  rnd_bg_color(), 1)
	# 清除画笔
	del draw
	region = (0, 0, max(last_right + left_space, 100 + left_space), height)
	# 裁切图片
	crop_img = img.crop(region)
	# 这里直接返回图片的data数据，符合网站验证码实际要求
	buffered = BytesIO()
	crop_img.save(buffered, format="png")
	# 获得base64的图片数据，但是不适合应用场景
	# return 'data:image/png;base64,' + base64.b64encode(buffered.getvalue()).decode(encoding="utf-8"), ret_code
	return buffered.getvalue(), ret_code

def verifycode(request):
	verifyCodeList = create_verification(max_size=34, length=5)
	request.session['verifycode'] = verifyCodeList[1] # 将验证码图片的数值存储进 session 里面,存入session，用于做进一步验证
	# print(verifyCodeList[1])
	return HttpResponse(verifyCodeList[0], 'image/png')
