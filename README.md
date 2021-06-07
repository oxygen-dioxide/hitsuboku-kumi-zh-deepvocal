# Hitsuboku Kumi Chn Deepvocal

**English** | [中文](README_zh.md)

[Github](https://github.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal) | 
[Gitee](https://gitee.com/oxygendioxide/hitsuboku-kumi-chn-deepvocal) | 
[Gitlab](https://gitlab.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal) | 
[Bitbucket](https://bitbucket.org/oxygendioxide/hitsuboku-kumi-chn-deepvocal)

Hitsuboku Kumi (筆墨クミ) is a UTAU virtual singer developed by Cubialpha. This project ports Hitsuboku Kumi Chinese CVVC voicebank to deepvocal. This is the first open-source deepvocal voicebank on Github.

According to Hitsuboku Kumi's [Terms of use](https://cubialpha.wixsite.com/koomstar/character), redistribution of voicebanks, editing of oto.ini and audio samples, and porting to other synthesis softwares are allowed without permission, so long as the name "Hitsuboku Kumi" is unchanged, "Cubialpha" is credited, a link to [this website](https://cubialpha.wixsite.com/koomstar) is included, and it is clearly stated that you have made edits.

If you like this voicebank, please give her a star.

## [Demo](https://github.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal/issues/1)
(花欺~沉睡在浮空的花海, Original Music:Cube^3, Lyric:雨狸, midi:卦者那啥子靈風)

## Download
[Github Release](https://github.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal/releases/latest)

[Tencent Weiyun](https://gitee.com/oxygendioxide/hitsuboku-kumi-chn-deepvocal/releases)

## Tech Specs
- 4 pitches (A3, D4, A4, D5)
- using Voicemith reclist
- provide dvtb1.1.6 and dvtb2.1.0 builds
- tail symbol: R
- vowel pause from [Hitsuboku Kumi Japanese Act4](https://cubialpha.wixsite.com/koomstar/act4): "!a" "a_!" etc
- vocal fry from [Hitsuboku Kumi Japanese Act4](https://cubialpha.wixsite.com/koomstar/act4): "'a" "'a_!" etc
- standalone consonants (only available in the dvtb1 build): p, f, t, k, q, x, c, s, ch, sh, r

See [feature list](feature.md) for details

## Changes to the audio samples
- The volume is Normalized to -9db

## How to build this
1. Download this project with the following command:
```
git clone https://github.com/oxygen-dioxide/hitsuboku-kumi-chn-deepvocal
```

2. Download and install [deepvocal toolbox](https://dl.deep-vocal.com/toolbox/Setup_DeepVocalToolBox_beta_2.1.0.zip)

3. Open kumi.dvtb with deepvocal toolbox. Click "Function→Build voice bank"

4. Click "Build Voice Model Files" to compile this voicebank.

5. Click "Build Voice Bank" to pack this voicebank. The packed voicebank will be output to .\bin folder.

## Links
[Deepvocal Official Site](deep-vocal.com)

[Deepvocal toolbox manual](https://drive.google.com/drive/folders/1kAlPZnSO9f4pv5wbVJUdNNQXZQOy6pGA?usp=sharing)

[Deepvocal Mark Tool (DVMT) repo](https://github.com/FangCunWuChang/DeepVocal-Mark-Tool)

[Hitsuboku Kumi Official Site](https://cubialpha.wixsite.com/koomstar)

[Cubialpha's bilibili channel](https://space.bilibili.com/522152972)