// axios 数据请求文件配置
// 主要是对axios的拦截器进行了配置
import axios from 'axios';
import qs from 'qs';

// 1. 初始化axios默认全局配置，该配置将会在所有请求中生效
// 超时设置
axios.defaults.timeout = 100000;
// 根据环境动态替换路径
axios.defaults.baseURL = process.env.VUE_APP_ServiceUrl;
// 设置post请求的请求头
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

// 2. 配置拦截器
// 2.1 配置请求拦截器---在请求发出前进行拦截
axios.interceptors.request.use(config => {
  config.headers['cache-control'] = `no-cache`;
  config.headers['Pragma'] = `no-cache`;
  // post请求对请求参数进行统一序列化，因为后台无法接受使用qs.stringify序列化后的参数，故改为如下序列方式，将数组序列化为字符串
  if (config.method === 'post') {
    let postData = JSON.parse(JSON.stringify(config.data));
    for (const [key, value] of Object.entries(postData)) {
      if (Array.isArray(value)) {
        postData[key] = JSON.stringify(value);
      }
    }
    config.data = postData;
    config.data = qs.stringify(config.data);
  }
  // console.log(config); // for debug
  return config;
}, error => {
  // 当出现请求错误时做一些事
  return Promise.reject(error);
});

// 2.2 配置响应拦截器---在请求响应后进行拦截
axios.interceptors.response.use(response => {
  // 在服务器对请求做出响应并返回数据后做一些事情
  return response.data;
}, error => {
  // 返回请求失败信息
  // console.log(JSON.stringify(error)) // for debug
  if (error && error.response) {
    switch (error.response.status) {
      case 400:
        error.message = '错误请求，状态码:400';
        break;
      case 401:
        error.message = '未授权，请重新登录，状态码:401';
        break;
      case 403:
        error.message = '拒绝访问，状态码:403';
        break;
      case 404:
        error.message = '请求错误,未找到该资源，状态码:404';
        break;
      case 405:
        error.message = '请求方法未允许，状态码:405';
        break;
      case 408:
        error.message = '请求超时，状态码:408';
        break;
      case 500:
        error.message = '服务器端出错，状态码:500';
        break;
      case 501:
        error.message = '网络未实现，状态码:501';
        break;
      case 502:
        error.message = '网络错误，状态码:502';
        break;
      case 503:
        error.message = '服务不可用，状态码:503';
        break;
      case 504:
        error.message = '网络超时，状态码:504';
        break;
      case 505:
        error.message = 'http版本不支持该请求，状态码:505';
        break;
      default:
        error.message = `连接错误${error.response.status}`;
    }
  } else {
    error.message = "连接到服务器失败";
  }
  return Promise.reject(error.message);
});

export default axios;
