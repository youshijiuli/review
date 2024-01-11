# day47作业（张珵）

# 一、时钟

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>张珵计时器</title>
</head>
<body>
    <input type="text" id="i1">
    <button id="b1">开始</button>
    <button id="b2">结束</button>
    <script>
        var b1 = document.getElementById('b1');
        var b2 = document.getElementById('b2');
        var interval_id;     // 声明一个全局变量
        b1.onclick = function(){
            // 当interval_id未定义时，开启时钟，并将其线程ID赋值给interval_id
            if (interval_id === undefined) {
                interval_id = setInterval(function () {
                    var d1 = new Date();
                    var i1 = document.getElementById('i1');
                    i1.value = d1.toLocaleString();
                }, 1000);
            };
        };
        b2.onclick = function(){
            // 当interval_id已定义时，关闭时钟，并将interval_id的值删除（变为未定义）
            if (interval_id !== undefined) {
                clearInterval(interval_id);
                interval_id = undefined;
            }
        }
    </script>
</body>
</html>
```

# 二、下拉菜单

## **张珵版**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>张珵下拉菜单</title>
</head>
<body>
    <select id='province'></select>
    <select id='city'></select>
    <script>

        // 定义函数：将对应的子标签添加到s2
        function s2_appendChild() {
            s2_options = data[s1.options[s1.selectedIndex].innerText];
            for (var k in s2_options) {
                var o2 = document.createElement('option');
                o2.innerText = s2_options[k];
                s2.appendChild(o2);
            }
        }

        var data = {"河北省": ["廊坊", "邯郸"], "北京": ["朝阳区", "海淀区"], "山东": ["威海市", "烟台市"]};
		s1 = document.getElementById('province');

        // 将对应的子标签添加到s1
        for (var i in data) {
            var o1 = document.createElement('option');
            o1.innerText = i;
            s1.appendChild(o1);
        }

        // 执行函数：将对应的子标签添加到s2，用于页面首次加载时（此时无事件发生）
        var s2 = document.getElementById('city')
        s2_appendChild();

        s1.onchange = function() {

            // 清除s2现有的子标签（这里必须倒序删除，否则有坑）
            s2_children = s2.children;
            for(var j = s2_children.length-1; j>=0; j--) {
                s2.removeChild(s2_children[j]);
            }

            // 执行函数：将对应的子标签添加到s2
            s2_appendChild()
        }

    </script>
</body>
</html>
```

## **老师答案**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>select联动</title>
</head>
<body>
<select id="province">
  <option>请选择省:</option>
</select>

<select id="city">
  <option>请选择市:</option>
</select>

<script>
  data = {"河北省": ["廊坊", "邯郸"], "北京": ["朝阳区", "海淀区"], "山东": ["威海市", "烟台市"]};

  var s1 = document.getElementById("province");
  var s2 = document.getElementById("city");
  //页面一刷新就将所有的省份都添加到select标签中
  for (var i in data) {
    var o1 = document.createElement("option"); //创建option标签
    o1.innerHTML = i; //将省份的数据添加到option标签中
    s1.appendChild(o1);//将option标签添加到select标签中
  }
  //只要select中选择的值发生变化的时候，就可以触发一个onchange事件，那么我们就可以通过这个事件来完成select标签联动
  
  s1.onchange = function () {
    //1.获取省的值
    var pro = (this.options[this.selectedIndex]).innerHTML;//this.selectedIndex是当前选择的option标签的索引位置，this.options是获取所有的option标签，通过索引拿到当前选择的option标签对象，然后.innerHTML获取对象中的内容，也就是省份
    //还可以这样获取省：var pro = this.value;
    var citys = data[pro]; //2. 通过上面获得的省份去data里面取出该省对应的所有的市
    // 3. 清空option
    s2.innerText = ""; //清空显示市的那个select标签里面的内容
　　
    //4.循环所有的市，然后添加到显示市的那个select标签中
    for (var i=0;i<citys.length;i++) {
      var o2 = document.createElement("option");
      o2.innerText = citys[i];
      s2.appendChild(o2);
    }
  }
</script>
</body>
</html>
```

