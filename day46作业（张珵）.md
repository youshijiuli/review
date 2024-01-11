DAY46作业：敲JAVASCRIPT代码

```javascript
var a = 10
undefined
a
10
typeof a
"number"
var a = 'abcdefg'
undefined
typeof a
"string"
typeOf a;
VM381:1 Uncaught SyntaxError: Unexpected identifier
typeOf a
VM389:1 Uncaught SyntaxError: Unexpected identifier
c=123e5
12300000
a='abc'
"abc"
b='edc'
"edc"
a+b
"abcedc"
a*2
NaN
c=a*2
NaN
console.log(c)
VM476:1 NaN
undefined
NaN
NaN
typeof NaN
"number"
parseInt('123')
123
parseInt('1A2B')
1
parseInt('1.8.9')
1
parsefloat('1.8.9.0\')
VM599:1 Uncaught SyntaxError: Invalid or unexpected token
parsefloat('1.8.9.0')
VM602:1 Uncaught ReferenceError: parsefloat is not defined
    at <anonymous>:1:1
(anonymous) @ VM602:1
b=parseInt(a)
NaN
var a='hello'
undefined
a.length
5
var a = ' a b c  '
undefined
a
" a b c  "
a.trim()
"a b c"
var a = ' a b c  '
undefined
a.trimLeft
ƒ trimStart() { [native code] }
a.trimLeft()
"a b c  "
a='abcdef'
"abcdef"
a[1]
"b"
a.charAt(1)
"b"
b='wold'
"wold"
a.concat(b)
"abcdefwold"
a
"abcdef"
a.indexOf(c)
-1
a.indexOf('c')
2
c='c'
"c"
a.indexOf(c)
2
a.indexOf(c,3)
-1
a.slice(2,4)
"cd"
a='abc|asdf|ewg|gsrgh|sfc'
"abc|asdf|ewg|gsrgh|sfc"
a.split('|')
(5) ["abc", "asdf", "ewg", "gsrgh", "sfc"]
a.split('|',3)
(3) ["abc", "asdf", "ewg"]
var a = (2>1)
undefined
a
true
(null === null)
true
(NaN===NaN)
false
(undefined === undefined)
true
typeof undefined\
VM1202:1 Uncaught SyntaxError: Invalid or unexpected token
typeof undefined
"undefined"
var a = new string('bb')
VM1240:1 Uncaught ReferenceError: string is not defined
    at <anonymous>:1:9
(anonymous) @ VM1240:1
var a = new String('bb')
undefined
var a = [11,22,33];
undefined
a
(3) [11, 22, 33]
var b = new Array([22,33])
undefined
typeof a
"object"
a[1]
22
console.log(a[1])
VM1454:1 22
undefined
a
(3) [11, 22, 33]
a.push(44)
4
a
(4) [11, 22, 33, 44]
a.pop()
44
a
(3) [11, 22, 33]
a.unshift(0)]\
VM1531:1 Uncaught SyntaxError: Unexpected token ]
a.unshift(0)]
VM1537:1 Uncaught SyntaxError: Unexpected token ]
a.unshift(0)
4
a
(4) [0, 11, 22, 33]
a.shift()
0
a
(3) [11, 22, 33]
var a=[11,4,73,84,111]
undefined
a.sort()
(5) [11, 111, 4, 73, 84]
a
(5) [11, 111, 4, 73, 84]
	function sortNumber(a,b){
    	return a - b;
	}
undefined
a.sort(sortNumber)
(5) [4, 11, 73, 84, 111]
var a = [84,72,11,4]
undefined
a.splice(1,2,'aa','bb','cc')
(2) [72, 11]
a
(5) [84, "aa", "bb", "cc", 4]
console.log(a)
VM1771:1 (5) [84, "aa", "bb", "cc", 4]
undefined
var a={name:'chao',age:18}
undefined
a
{name: "chao", age: 18}
var a={'name':'chao','age':18}
undefined
a
{name: "chao", age: 18}
for (var i in a){console.log(i,a[i]}
VM1881:1 Uncaught SyntaxError: missing ) after argument list
for (var i in a){console.log(i,a[i])}
VM1886:1 name chao
VM1886:1 age 18
undefined
var a = 10;
if (a > 5){   
  console.log("a > 5");
}else if (a < 5) {
  console.log("a < 5");
}else {
  console.log("a = 5");
}
VM1889:3 a > 5
undefined

var a = 11;
undefined
switch (a){    //switch (a++){}
    case 9:
		console.log('999');
	break;
    case 10:
		console.log('101010');
	break;
    case 11:
		console.log('111111');
	break;
}
VM1893:12 111111
undefined

var a = 11;
switch (a++){    //switch (a++){}
    case 9:
		console.log('999');
	break;
    case 10:
		console.log('101010');
	break;
    case 11:
		console.log('111111');
	break;
}
VM1901:11 111111
undefined

var a = 9;
switch (a++){    //switch (a++){}
    case 9:
		console.log('999');
	break;
    case 10:
		console.log('101010');
	break;
    case 11:
		console.log('111111');
	break;
}
VM1906:5 999
undefined

var a = 9;
switch (a++){    //switch (a++){}
    case 9:
		console.log('999');
	break;
    case 10:
		console.log('101010');
	break;
    case 11:
		console.log('111111');
	break;
}
VM1908:5 999
undefined
    var a = 20;

    switch (a){
        case 9:
            console.log('999');
        break;
        case 10:
            console.log('101010');
        break;
        case 11:
            console.log('111111');
        break;
        default :  //上面的条件都不成立的时候,走default
            console.log('啥也不对!!')

    }
VM1911:14 啥也不对!!
undefined
for (var i=0;i<10;i++) {  
  console.log(i);
}
VM1914:2 0
VM1914:2 1
VM1914:2 2
VM1914:2 3
VM1914:2 4
VM1914:2 5
VM1914:2 6
VM1914:2 7
VM1914:2 8
VM1914:2 9
undefined
var i = 0;
while (i < 10) {
  console.log(i);
  i++;
}
VM1917:3 0
VM1917:3 1
VM1917:3 2
VM1917:3 3
VM1917:3 4
VM1917:3 5
VM1917:3 6
VM1917:3 7
VM1917:3 8
VM1917:3 9
9
var i = 0;
while (i < 10) {
  console.log(i);
  i++;
}
VM1920:3 0
VM1920:3 1
VM1920:3 2
VM1920:3 3
VM1920:3 4
VM1920:3 5
VM1920:3 6
VM1920:3 7
VM1920:3 8
VM1920:3 9
9
(function(a, b){
  return a + b;
})(1, 2); 
3
var city = "BeiJing";
function f(){
    var city = "ShangHai";
    function inner(){
        console.log(city);
    }
    return inner;
}
var ret = f();
undefined
ret
ƒ inner(){
        console.log(city);
    }
ret()
VM1926:5 ShangHai
undefined
function Person(name){
	this.name = name;
}
var p = new Person('taibai');
p.name
"taibai"
Person.prototype.sum = function(a,b){return a+b;}
ƒ (a,b){return a+b;}
VM1950:2 Uncaught SyntaxError: Unexpected token {
Person.prototype.sum = function(a,b){return a+b;}
ƒ(a,b){return a+b;}
VM1953:2 Uncaught SyntaxError: Unexpected token {
Person.prototype.sum = function(a,b){return a+b;}
ƒ (a,b){return a+b;}
p.sum(2,3);
5
var d1 = new Date()
undefined
d1
Wed Jul 03 2019 22:21:03 GMT+0800 (中国标准时间)
console.log(d1.toLocaleString())
VM1972:1 2019/7/3 下午10:21:03
undefined
var d2 = new Date("2004/3/20 11:12");
console.log(d2.toLocaleString());
VM1975:2 2004/3/20 上午11:12:00
undefined
var d3 = new Date("04/03/20 11:12");
undefined
console.log(d3.toLocaleString());
VM1981:1 2020/4/3 上午11:12:00
undefined
var d3 = new Date(5000);  
console.log(d3.toLocaleString());
console.log(d3.toUTCString());  
VM1984:2 1970/1/1 上午8:00:05
VM1984:3 Thu, 01 Jan 1970 00:00:05 GMT
undefined
var d4 = new Date(2004,2,20,11,12,0,300);
console.log(d4.toLocaleString());  
VM1987:2 2004/3/20 上午11:12:00
undefined
var d = new Date()
undefined
d
Wed Jul 03 2019 22:22:31 GMT+0800 (中国标准时间)
getDate()     
VM2000:1 Uncaught ReferenceError: getDate is not defined
    at <anonymous>:1:1
(anonymous) @ VM2000:1
getDate()
VM2011:1 Uncaught ReferenceError: getDate is not defined
    at <anonymous>:1:1
(anonymous) @ VM2011:1
var d = new getDate() 
VM2036:1 Uncaught ReferenceError: getDate is not defined
    at <anonymous>:1:9
(anonymous) @ VM2036:1
var d = new getDate()
VM2043:1 Uncaught ReferenceError: getDate is not defined
    at <anonymous>:1:9
(anonymous) @ VM2043:1
var str1 = '{"name": "chao", "age": 18}';
var obj1 = {"name": "chao", "age": 18};
undefined
var obj = JSON.parse(str1); 
undefined
var str = JSON.stringify(obj1);
undefined
obj
{name: "chao", age: 18}
str
"{"name":"chao","age":18}"
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
undefined
var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/
undefined
var s = 'hello'
	reg1.test(s)
false
reg1.test()
true
var s2 = "hello world";
undefined
s2.match(/o/g);
(2) ["o", "o"]
s2.search(/h/g);  

0
s2.split(/o/g); 
(3) ["hell", " w", "rld"]
s2.replace(/o/g, "s"); 
"hells wsrld"
var s1 = "name:Alex age:18";
undefined
s1.replace(/a/, "哈哈哈");
"n哈哈哈me:Alex age:18"
s1.replace(/a/g, "哈哈哈");
"n哈哈哈me:Alex 哈哈哈ge:18"
s1.replace(/a/gi, "哈哈哈");
"n哈哈哈me:哈哈哈lex 哈哈哈ge:18"
	var reg = /a/g;
	var s = 'alex a sb';
	reg.test(s); 
true
reg.lastIndex; 
1
reg.test(s);
true
reg.lastIndex; 
6
reg.test(s);
false
reg.lastIndex = 0
0
reg.test(s);

true
reg.test(s);
true
reg.lastIndex; 
6
reg.lastIndex = 0
0
reg.test(s);
true
Math.abs(-1)
1
Math.exp(1)
2.718281828459045
Math.floor(1.99、)
VM2179:1 Uncaught SyntaxError: missing ) after argument list
Math.floor(1.99)
1
Math.log(1) 
0
Math.max(1,2) 
2
Math.min(1,2) 
1
Math.pow(3,2) 
9
Math.random() 
0.13446132450791537
Math.round(4.5)
5
Math.sin(90)
0.8939966636005579
Math.sin(3.1415926535897932)
1.2246467991473532e-16
Math.sqrt(-1)
NaN
Math.sqrt(2)
1.4142135623730951
Math.tan(3.1415926535897932)
-1.2246467991473532e-16
```

