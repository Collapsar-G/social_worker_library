<template>
    <div class="home">
        <!-- 服务器错误提示-->
        <div v-if="warncard">
            <v-alert
                    icon="mdi-cloud-alert"
                    prominent
                    text
                    type="error"
            >
                找不到服务器，请检查网络或者刷新重试
            </v-alert>
        </div>

        <div v-if="!warncard">
            <!--            开始一条新的查询模块-->
            <v-col>

                <v-container>
                    <v-row dense>
                        <v-col cols="12">
                            <v-card
                                    color=
                                            dark
                            >
                                <v-card-title class="headline">
                                    数据源：GroupData
                                </v-card-title>


                                <v-card-subtitle>
                                    请输入QQ号或者QQ群号进行查找(可选填)
                                </v-card-subtitle>
                                <v-spacer></v-spacer>
                                <!--                            <a>{{config.GroupData.search_key.QQNum}}</a>-->
                                <!--                            <a>{{config.GroupData.search_key.QunNum}}</a>-->
                                <v-col class=".col-md-6 .offset-md-3">
                                    <v-text-field
                                            counter="15"
                                            full-width
                                            label="QQNum"
                                            v-model="config.GroupData.search_key.QQNum"
                                    ></v-text-field>
                                    <v-text-field
                                            counter="15"
                                            label="QunNum"
                                            v-model="config.GroupData.search_key.QunNum"

                                    ></v-text-field>
                                    <v-card
                                            class="mx-auto"
                                            color="#ECEFF1"
                                            width="100px"
                                    >
                                        <v-btn
                                                :disabled="leading"
                                                :loading="leading"
                                                @click="submit_data_GroupData"
                                                class="mx-auto"
                                                color="#ECEFF1"
                                                elevation="4"
                                                large
                                                width="100px"
                                        >查找
                                        </v-btn>
                                        <v-spacer></v-spacer>
                                        <v-spacer></v-spacer>
                                    </v-card>
                                    <v-spacer></v-spacer>
                                    <v-spacer></v-spacer>
                                    <a> </a>
                                    <p></p>
                                    <div v-if="error_qq">
                                        <v-alert
                                                icon="mdi-cloud-alert"
                                                prominent
                                                text
                                                type="error"
                                        >
                                            参数不能为空
                                        </v-alert>
                                    </div>
                                    <div v-if="result_groupdata.code === 200">

                                        <v-treeview>
                                            查询结果
                                            <v-data-table
                                                    :headers="result_groupdata.headers"
                                                    :items="result_groupdata.desserts"
                                                    :items-per-page="5"
                                                    class="elevation-1"
                                            ></v-data-table>
                                        </v-treeview>
                                    </div>
                                    <div v-if="result_groupdata.code === 300">

                                        <v-alert
                                                dense
                                                prominent
                                                text
                                                type="info"
                                        >
                                            {{result_groupdata.msg}}
                                        </v-alert>
                                    </div>
                                </v-col>

                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
            <!--<分界线     一个搜索模块-->
            <v-col>

                <v-container>
                    <v-row dense>
                        <v-col cols="12">
                            <v-card
                                    color=
                                            dark
                            >
                                <v-card-title class="headline">
                                    数据源：QunInfo
                                </v-card-title>


                                <v-card-subtitle>
                                    请输入QQ群号进行查找
                                </v-card-subtitle>
                                <v-spacer></v-spacer>

                                <v-col class=".col-md-6 .offset-md-3">
                                    <v-text-field
                                            counter="15"
                                            label="QunNum"
                                            v-model="config.QunInfo.search_key.QunNum"

                                    ></v-text-field>
                                    <v-card
                                            class="mx-auto"
                                            color="#ECEFF1"
                                            width="100px"
                                    >
                                        <v-btn
                                                :disabled="leading"
                                                :loading="leading"
                                                @click="submit_data_QunInfo"
                                                class="mx-auto"
                                                color="#ECEFF1"
                                                elevation="4"
                                                large
                                                width="100px"
                                        >查找
                                        </v-btn>
                                        <v-spacer></v-spacer>
                                        <v-spacer></v-spacer>
                                    </v-card>
                                    <v-spacer></v-spacer>
                                    <v-spacer></v-spacer>
                                    <a> </a>
                                    <p></p>
                                    <div v-if="error_qun">
                                        <v-alert
                                                icon="mdi-cloud-alert"
                                                prominent
                                                text
                                                type="error"
                                        >
                                            参数不能为空
                                        </v-alert>
                                    </div>
                                    <div v-if="result_quninfo.code === 200">
                                        <v-card-subtitle>
                                            查询结果：
                                        </v-card-subtitle>
                                        <v-data-table
                                                :headers="result_quninfo.headers"
                                                :items="result_quninfo.desserts"
                                                :items-per-page="5"
                                                class="elevation-1"
                                        ></v-data-table>
                                    </div>
                                    <div v-if="result_quninfo.code === 300">

                                        <v-alert
                                                dense
                                                prominent
                                                text
                                                type="info"
                                        >
                                            {{result_quninfo.msg}}
                                        </v-alert>
                                    </div>
                                </v-col>

                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
            <!-- 一个搜索模块-->
        </div>
    </div>


</template>

<script>
    // @ is an alias to /src
    import url from '../components/url.vue'

    export default {
        name: 'Home',
        data: () => ({
            leading: false,
            warncard: false,
            happy: false,
            error_qq: false,
            error_qun: false,
            globalHttpUrl: url.httpUrl,
            config: {
                "GroupData": {
                    "result_class": {
                        "Age": "",
                        "Auth": "",
                        "Gender": "",
                        "Nick": "",
                        "QQNum": "",
                        "QunNum": "",
                        "id": ""
                    },
                    "search_key": {
                        "QQNum": "",
                        "QunNum": ""
                    }
                },
                "QunInfo": {
                    "result_class": {
                        "Class": "",
                        "CreateDate": "",
                        "MastQQ": "",
                        "QunNum": "",
                        "QunText": "",
                        "Title": "",
                        "id": ""
                    },
                    "search_key": {
                        "QunNum": ""
                    }
                }
            },

            result_groupdata: [],
            result_quninfo: []
        }),
        // created() {
        //     this.clc();
        // },
        methods: {
            submit_data_QunInfo() {
                let that = this
                that.leading = true
                that.happy = false
                that.result_quninfo.code = 400
                that.error_qun = false
                if (that.config.QunInfo.search_key.QunNum !== "") {
                    console.log("@@@@@@@@@@@@@@")


                    this.axios.post(that.globalHttpUrl + 's/search/', {
                        "database": "QunInfo",
                        "QunNum": that.config.QunInfo.search_key.QunNum
                    }).then((response) => {
                        console.log(response.data)
                        console.log(that.config.QunInfo.search_key)
                        if (response.data.code === 200) {
                            that.result_quninfo = response.data
                            that.result_quninfo.headers = [
                                {
                                    text: 'QunNum',
                                    align: 'start',
                                    sortable: true,
                                    value: 'qunnum',
                                },
                                {text: 'MastQQ', value: 'mastqq'},
                                {text: 'CreateDate', value: 'createdata'},
                                {text: 'Title', value: 'tittle'},
                                {text: 'Class', value: 'class'},
                                {text: 'QunText', value: 'quntext'},
                            ]
                            that.result_quninfo.desserts = []
                            for (var datai in that.result_quninfo.data) {
                                var temp = {}
                                temp.qunnum = that.result_quninfo.data[datai][1]
                                temp.mastqq = that.result_quninfo.data[datai][2]
                                temp.createdata = that.result_quninfo.data[datai][3]
                                temp.tittle = that.result_quninfo.data[datai][4]
                                temp.class = that.result_quninfo.data[datai][5]
                                temp.quntext = that.result_quninfo.data[datai][6]
                                that.result_quninfo.desserts.push(temp)
                                // console.log("!!!!!!!!!!!!!!!!!!!!!")
                                // console.log(that.result_groupdata.data[datai])
                            }
                            console.log(that.result_quninfo)
                        } else if (response.data.code === 300) {
                            that.happy = true
                            that.result_quninfo = response.data
                        }

                        that.leading = false

                    }).catch((response) => {
                        console.log("fail", response);
                        that.leading = false
                        that.warncard = true
                    })
                } else {
                    that.error_qun = true
                    that.leading = false
                    that.happy = false
                    that.result_quninfo.code = 400
                }


            },
            submit_data_GroupData() {
                let that = this
                that.leading = true
                that.happy = false
                that.result_groupdata.code = 400
                that.error_qq = false
                if ((that.config.GroupData.search_key.QunNum !== "") || (that.config.GroupData.search_key.QQNum !== "")) {
                    console.log("@@@@@@@@@@@@@@")

                    this.axios.post(that.globalHttpUrl + 's/search/', {
                        "database": "GroupData",
                        "QunNum": that.config.GroupData.search_key.QunNum,
                        "QQNum": that.config.GroupData.search_key.QQNum
                    }).then((response) => {
                        console.log(response.data)
                        console.log(that.config.GroupData.search_key)
                        if (response.data.code === 200) {
                            that.result_groupdata = response.data
                            that.result_groupdata.headers = [
                                {
                                    text: 'QQNum',
                                    align: 'start',
                                    sortable: true,
                                    value: 'qqnum',
                                },
                                {text: 'Nick', value: 'nick'},
                                {text: 'Age', value: 'age'},
                                {text: 'Gender', value: 'gender'},
                                {text: 'Auth', value: 'auth'},
                                {text: 'QunNum', value: 'qunnum'},
                            ]
                            that.result_groupdata.desserts = []
                            for (var datai in that.result_groupdata.data) {
                                var temp = {}
                                temp.qqnum = that.result_groupdata.data[datai][1]
                                temp.nick = that.result_groupdata.data[datai][2]
                                temp.age = that.result_groupdata.data[datai][3]
                                temp.gender = that.result_groupdata.data[datai][4]
                                temp.auth = that.result_groupdata.data[datai][5]
                                temp.qunnum = that.result_groupdata.data[datai][6]
                                that.result_groupdata.desserts.push(temp)
                                // console.log("!!!!!!!!!!!!!!!!!!!!!")
                                // console.log(that.result_groupdata.data[datai])
                            }
                            console.log(that.result_groupdata)
                        } else if (response.data.code === 300) {
                            that.happy = true
                            that.result_groupdata = response.data

                        }

                        that.leading = false

                    }).catch((response) => {
                        console.log("fail", response);
                        that.leading = false
                        that.warncard = true
                    })
                } else {
                    that.error_qq = true
                    that.leading = false
                    that.happy = false
                    that.result_groupdata.code = 400
                }
            },
            clc() {
                let that = this
                this.leading = true
                // let params = new FormData()
                // params.append('imageData', this.imageData)
                this.axios.post(that.globalHttpUrl + 's/config/', {}).then((response) => {
                    console.log(response.data)
                    if (response.data.code === 200) {
                        // that.config = response.data.config
                        // for (var dbkeys in that.config) {
                        //     var temp = that.config[dbkeys]
                        //     // var temp = that.config[0]
                        //     that.dblist.push(temp)
                        //     that.dbname.push(dbkeys)
                        // }

                    } else {
                        that.warncard = true
                    }

                    that.leading = false

                }).catch((response) => {
                    console.log("fail", response);
                    that.leading = false
                    that.warncard = true
                })
            }
        }
    }
</script>
