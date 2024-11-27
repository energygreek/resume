# 使用模板生成简历
用模板生成简历，只关注内容不操心外观。使用git workspace 管理不同的版本简历，方便针对不同岗位投递。

## install 只依赖强大流行的jinja
pip install jinja
## Usage
1. Update resume.json in resume dir
2. python main.py gen

## 多语言支持
* 默认是英文简历， 其他语言也可以类似添加，当然只是模板语言而已。resume.json需自己翻译。
* 生成中文简历： python main.py gen -l zh_CN

## 更新简历模板
模板是两列的，不满意可以自行修改。如果增加了翻译， 需要同时更新翻译文件。 更新前先安装`gettext`， 如"sudo apt install gettext -y"

### 更新英文
1. 更新po文件， python main.py collectmsg -l en_US
2. 补充msgstr
3. 生成mo, msgfmt lang/en_US/LC_MESSAGES/resume.po -o lang/en_US/LC_MESSAGES/resume.mo

### 更新中文
1. 更新po文件， python main.py collectmsg -l zh_CN
2. 补充msgstr
3. 生成mo, msgfmt lang/zh_CN/LC_MESSAGES/resume.po -o lang/zh_CN/LC_MESSAGES/resume.mo
