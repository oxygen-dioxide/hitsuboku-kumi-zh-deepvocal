# hitsuboku-kumi-chn-deepvocal
[English](README.md) | **中文**
## 关于本项目
Hitsuboku Kumi (筆墨クミ)是Cubialpha制作的UTAU虚拟歌手。本项目将Hitsuboku Kumi的中文CVVC音源移植到deepvocal引擎。这是Github上首个开源deepvocal音源。

根据Hitsuboku Kumi的[用户协议](https://cubialpha.wixsite.com/koomstar/character)，二次分发，修改oto.ini和音频文件，以及移植到其他合成引擎是允许的，只要保持名称"Hitsuboku Kumi"不变，署名"Cubialpha"，提供[官网链接](https://cubialpha.wixsite.com/koomstar)，并明确说明你做了编辑。

## 技术规格
- 4音阶 (A3, D4, A4, D5)
- 使用飞天胶囊录音表

## 对音频的修改
- 音量标准化到-9db

## 自行编译本项目
1. 用以下命令下载本项目：
```
git clone https://github.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal
```

2. 下载并安装[deepvocal toolbox](https://dl.deep-vocal.com/toolbox/Setup_DeepVocalToolBox_beta_2.1.0.zip)

3. 用deepvocal toolbox打开kumi.dvtb，点击“Function→Build voice bank”，将wav locations、model file location和voice bank location均设为下载位置。
例如，如果你将项目下载到了C:\hitsuboku-kumi-chn-deepvocal,则你需要如图设置：
![](Resource/2021-05-26-16-53-26.png)

4. 点击“Build Voice Model Files”，编译音源。

5. 点击“Build Voice Bank”，打包音源。

## 相关链接
[Deepvocal 官网](deep-vocal.com)

[Deepvocal toolbox 使用说明](https://share.weiyun.com/5snXMol)

[Hitsuboku Kumi官网](https://cubialpha.wixsite.com/koomstar)