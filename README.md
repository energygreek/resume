# 使用模板生成简历
## install jinja
pip install jinja
## Usage
* Update resume json file in resume dir
* python main.py gen

## 多语言支持
默认是英文简历，其他语言也可以类似添加。先安装依赖如"sudo apt install gettext -y"
生成中文简历: python main.py gen -l zh_CN

## 更新简历模板
如果对模板文件的翻译部分更改，需要同时更新翻译文件

### 更新英文
1. 更新po文件， python main.py collectmsg -l en_US
2. 补充翻译目标内容
3. 生成mo, msgfmt lang/en_US/LC_MESSAGES/resume.po -o lang/en_US/LC_MESSAGES/resume.mo

### 更新中文
1. 更新po文件， python main.py collectmsg -l zh_CN
2. 补充翻译目标内容
3. 生成mo, msgfmt lang/zh_CN/LC_MESSAGES/resume.po -o lang/zh_CN/LC_MESSAGES/resume.mo
