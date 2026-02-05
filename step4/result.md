```md
 python3 -m step4.print_tree https://browser.engineering/html.html
 <!DOCTYPE html>
   '\n'
   <html lang="en-US" xml:lang="en-US">
     '\n'
     <head>
       '\n  '
       <meta charset="utf-8" />
         '\n  '
         <meta name="color-scheme" content="dark light">
```

- 추가적인 파싱 처리를 통해, 아래와 같이 해결 가능

```py
python3 -m step4.print_tree https://browser.engineering/html.html
 <html lang="en-US" xml:lang="en-US">
   <head>
```

```py
(base) coder@enthusiasticui-MacBookPro under-browser % python3 -m step4.print_tree https://browser.engineering/html.html
 <html>
   <head>
     <meta>
     <meta>
     <meta>
     <link>
     <link>
     <link>
     <link>
     <link>
     <link>
     <link>
     <link>
     <link>
     <link>
     <meta>
```


## 4.6 암시적 태그 검증

python -m step2.tk-browser  https://browser.engineering/