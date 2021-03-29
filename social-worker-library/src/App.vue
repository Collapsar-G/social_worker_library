<template>
    <v-app>
        <v-app-bar
                app
                color="blue-grey lighten-2"
                dark
        >
            <div class="d-flex align-center">
                <v-img
                        alt="Vuetify Logo"
                        class="shrink mr-2"
                        contain
                        src="https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20201214234732.png"
                        transition="scale-transition"
                        width="80"
                />

                <v-img
                        alt="Vuetify Name"
                        class="shrink mt-1 hidden-sm-and-down"
                        contain
                        min-width="100"
                        src="https://cdn.jsdelivr.net/gh/Collapsar-G/image/img/20210316110537.png"
                        width="300"
                />
            </div>

            <v-spacer>

            </v-spacer>
            <v-tabs
                    align-with-title

                    color="white"
            >
                <v-tabs-slider color="white"/>
                <v-tab @click="toQQGroupSearch">数据查询及其可视化</v-tab>
                <v-tab @click="toHelloWorld">数据可视化</v-tab>
                <v-tab @click="toAntv">数据可视化 2.0</v-tab>
<!--                <v-tab @click="totest">test</v-tab>-->
            </v-tabs>
            <v-btn
                    href="https://www.zhihu.com/question/27024854"
                    target="_blank"
                    text
            >
                <span class="mr-2">Be careful!</span>
                <v-icon>mdi-open-in-new</v-icon>
            </v-btn>
        </v-app-bar>

        <v-main>
            <v-alert
                    border="top"
                    colored-border
                    elevation="2"
                    type="warning"
            >
                <div class="text-lg-center">
                    <a style="color: #FFA726">
                        仅用于《系统安全》课程学习,请勿用于非法用途!!!
                    </a>

                </div>


            </v-alert>
            <!-- 不用于非法用途提示-->
            <div class="text-center">
                <v-dialog
                        v-model="dialog"
                        width="500"
                >

                    <v-card>
                        <v-card-text>

                        </v-card-text>

                        <v-card-text>
                            <a style="color: #FFA726">仅用于学习使用,不将数据用于非法用途!!!</a>
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                    @click="dialog = false"
                                    color="#FFA726"
                                    text
                            >
                                I accept
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </div>

                <router-view v-if="connect"></router-view>
                <div v-if="!connect">
            <v-alert
                    icon="mdi-cloud-alert"
                    prominent
                    text
                    type="error"
            >
                找不到服务器，请检查网络或者刷新重试
            </v-alert>
        </div>

        </v-main>
        <v-footer
                dark
                padless
        >
            <v-card
                    class="flex"
                    flat
                    tile
            >


                <!--                <v-card-text class="blue-grey darken-2 white&#45;&#45;text text-center">-->
                <!--                    仅用于《系统安全》课程学习<br>请勿用于非法用途-->
                <!--                </v-card-text>-->
                <v-divider></v-divider>
                <v-card-text class="py-2 white--text text-center">
                    Copyright © {{ new Date().getFullYear() }} <strong>Collapsar-G</strong>. All rights reserved.
                </v-card-text>
            </v-card>
        </v-footer>
    </v-app>
</template>

<script>

import url from './components/url.vue'
    export default {
        name: 'App',

        components: {},

        data: () => ({
            dialog: true,
            connect: false,
            globalHttpUrl: url.httpUrl,
        }), created() {
            this.testconnect();
        },
        methods: {
            toQQGroupSearch() {
                this.$router.push({path: './'})
            },
            toAntv() {
                this.$router.push({path: './antv'})
            },
            // totest() {
            //     this.$router.push({path: './test'})
            // },
            toHelloWorld() {
                this.$router.push({path: './about'})
            },
            testconnect() {
                let that = this
                this.connect = false
                // let params = new FormData()
                // params.append('imageData', this.imageData)
                this.axios.post(that.globalHttpUrl+'s/', {}).then((response) => {
                    console.log(response.data)
                    if (response.data.code === 200) {
                        that.connect = true
                        console.log(that.connect)

                    } else {
                        that.connect = false
                    }

                }).catch((response) => {
                    console.log("fail", response);
                    that.connect = false
                })
            }

        }
    };
</script>
