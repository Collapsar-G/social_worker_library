<template>
    <div class="about">
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
        <div v-if="leading">
            <v-alert
                    border="left"
                    color="teal"
                    dense
                    icon="mdi-clock-fast"
                    text
            >
                数据查询中，请您耐心等待！！
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
                                    请输入QQ号或者QQ群号进行可视化(二选一,都填写默认使用QQ号)
                                </v-card-subtitle>
                                <v-spacer></v-spacer>
                                <!--                            <a>{{config.GroupData.search_key.QQNum}}</a>-->
                                <!--                            <a>{{config.GroupData.search_key.QunNum}}</a>-->
                                <v-col class=".col-md-6 .offset-md-3">
                                    <v-text-field
                                            counter="15"
                                            full-width
                                            label="QQNum"
                                            v-model="QQNum"
                                    ></v-text-field>
                                    <v-text-field
                                            counter="15"
                                            label="QunNum"
                                            v-model="QunNum"

                                    ></v-text-field>

                                    <v-card
                                            class="mx-auto"
                                            color="#ECEFF1"
                                            width="100px"
                                    >
                                        <v-btn
                                                :disabled="leading"
                                                :loading="leading"

                                                @click="submit_data()"
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
                                    <v-spacer></v-spacer>
                                    <v-spacer></v-spacer>
                                    <p></p>
                                    <p></p>
                                    <div v-if="error">
                                        <v-alert
                                                icon="mdi-cloud-alert"
                                                prominent
                                                text
                                                type="error"
                                        >
                                            参数不能为空
                                        </v-alert>
                                    </div>
                                    <div v-if="result.code === 200">
                                        <v-card
                                                class="mx-auto"
                                                color="#ECEFF1"
                                                width="1000px"
                                        >
                                            <v-img
                                                    :src="img"

                                                    contain
                                                    max-height="600"
                                                    max-width="1000"
                                            ></v-img>
                                        </v-card>
                                        <v-spacer></v-spacer>
                                        <v-spacer></v-spacer>
                                        <a> </a>
                                        <v-spacer></v-spacer>
                                        <v-spacer></v-spacer>
                                        <p></p>
                                        <p></p>
                                        <v-treeview>

                                            <v-spacer>图例:</v-spacer>
                                            <p></p>
                                            <v-data-table
                                                    :headers="result.headers"
                                                    :items="result.desserts"
                                                    :items-per-page="5"
                                                    class="elevation-1"
                                            ></v-data-table>
                                        </v-treeview>
                                    </div>
                                    <div v-if="result.code === 300">

                                        <v-alert
                                                dense
                                                prominent
                                                text
                                                type="info"
                                        >
                                            {{result.msg}}
                                        </v-alert>
                                    </div>
                                </v-col>

                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
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
            result: [],
            QQNum: "",
            QunNum: "",
            error: false,
            globalHttpUrl: url.httpUrl,
            img: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAXIaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA2LjAtYzAwMiA3OS4xNjQzNTIsIDIwMjAvMDEvMzAtMTU6NTA6MzggICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMS4xIChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjAtMDUtMThUMTc6Mjk6MDQrMDg6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjAtMDUtMThUMTc6Mjk6MDQrMDg6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDIwLTA1LTE4VDE3OjI5OjA0KzA4OjAwIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmQxZWY5MDJjLTQ3YTMtOTM0Zi05NGY0LWU0Y2M4ZTgwODEzOCIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9z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"
        }),
        methods: {
            init() {
                let that = this
                that.leading = true
                that.happy = false
                that.error = false
                that.result.code = 400
            },
            submit_data() {
                let that = this
                that.leading = true
                that.happy = false
                that.error = false
                that.result.code = 400
                var key = ""
                var value = ""
                if (that.QQNum !== "") {
                    key = "QQNum"
                    value = that.QQNum
                } else if (that.QunNum !== "") {
                    key = "QunNum"
                    value = that.QunNum
                } else {
                    that.error = true
                    that.leading = false
                    that.result.code = 400
                    return
                }
                console.log(value, key)
                this.axios.post(that.globalHttpUrl + 'v/visualization/', {
                    "key": key,
                    "value": value
                }).then((response) => {
                    console.log(value, key)
                    console.log(response.data)
                    if (response.data.code === 200) {
                        that.result = response.data
                        that.img = response.data.image
                        that.result.headers = [
                            {
                                text: 'Labels',
                                align: 'start',
                                sortable: true,
                                value: 'labels',
                            },
                            {text: 'Informations', value: 'informations'},
                        ]
                        that.result.desserts = []
                        for (var datai in that.result.id2data) {
                            var temp = {}
                            temp.labels = datai
                            temp.informations = that.result.id2data[datai]
                            that.result.desserts.push(temp)
                            // console.log("!!!!!!!!!!!!!!!!!!!!!")
                            // console.log(that.result_groupdata.data[datai])
                        }
                        console.log(that.result)
                    } else if (response.data.code === 300) {
                        that.happy = true
                        that.result = response.data
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