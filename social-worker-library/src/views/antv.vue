<template>
    <div class="antv">
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

                                                @click="posturl()"
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
                                    <div>
                                        <v-card
                                                class="mx-auto"
                                                color="#ECEFF1"
                                                width="1000px"
                                        >

                                            <div>
                                                <div id="container"></div>
                                            </div>

                                        </v-card>


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
    import G6 from '@antv/g6';
    import url from '../components/url.vue'

    export default {
        mounted() {
            this.graph = this.initComponent();
        },
        data() {
            return {
                msg: "",
                chart: null,
                globalHttpUrl: url.httpUrl,
                leading: false,
                warncard: false,

                happy: false,
                // result: [],
                result: {
                    "code": 200,
                    "msg": "successful!",
                    "result_data": {
                        "edges": [
                            {
                                "source": "QQNum:100000",
                                "target": "QunNum:20025566",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100000",
                                "target": "QunNum:20059682",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100000",
                                "target": "QunNum:30084997",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100000",
                                "target": "QunNum:932145",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100000",
                                "target": "QunNum:988810",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:100000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:109320460",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:11011069",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:114824187",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:116136342",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:120733347",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:121340463",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:125036152",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:130004600",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:13108757",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:251153128",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:26590802",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:26659440",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:27201048",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:33032130",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:34460511",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:34781859",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:35783511",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:39928570",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:405915576",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:41131998",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:41636634",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:42295287",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:442190990",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:450459444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:453406757",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:45869842",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:46441534",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:47637682",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:47806092",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:48999402",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:49023633",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:51731123",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:520039345",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:55790383",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:563477417",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:57143487",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:57296897",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:57545731",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:57602236",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:75492822",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:764731426",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:76885152",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:7789513",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:85537545",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:879504324",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:8833250",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:888888",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:970190109",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20025566",
                                "target": "QQNum:99328126",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:100000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:243485682",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:285306062",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:330219985",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:345279146",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:346093802",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:379034431",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:415879901",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:504523551",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:516822314",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:517398439",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:532272331",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:640595342",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:654014044",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:75812591",
                                "value": 1
                            },
                            {
                                "source": "QunNum:20059682",
                                "target": "QQNum:762133202",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:100000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:200000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:200730082",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:200892613",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:243508740",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:26919126",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:294404987",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:297183460",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:300000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:308015274",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:337934627",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:343937090",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:393391583",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:397678912",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:400000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:408934138",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:491828974",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:500000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:525321435",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:532998334",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:546054621",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:549384276",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:584643897",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:598733008",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:600000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:644723605",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:700000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:739983900",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:748139333",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:758810096",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:800000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:807922095",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:815751507",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:819579741",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:823860591",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:83663647",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:857066092",
                                "value": 1
                            },
                            {
                                "source": "QunNum:30084997",
                                "target": "QQNum:900000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:100000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10000000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:100001",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10271",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10817",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10916",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10927",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:10937",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:11110",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:11114",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:11213",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:11999",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:1234567",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:14444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:200000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:21111",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:22221",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:22224",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:22225",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:300000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:30303030",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33331",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33332",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33334",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33335",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33336",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33337",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:33338",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:37777",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:400000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:43210",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44440",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44441",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:444444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44445",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44446",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44447",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:44448",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:45555",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:49999",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:500000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:51111",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:54444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55551",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55552",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55554",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:555555",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55556",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55557",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:55588",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:600000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:619951999",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:62222",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:64444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:65432",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:66661",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:66663",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:66667",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:66669",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:67777",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:700000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:71111",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:72222",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:73333",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:74444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77770",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77771",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77772",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77773",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77775",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77776",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77778",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:77779",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:78888",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:800000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:81111",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:82222",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:83333",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:84444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:85630",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:88788",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:88800",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:88884",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:88885",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:88887",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:888888",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:900000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:92222",
                                "value": 1
                            },
                            {
                                "source": "QunNum:932145",
                                "target": "QQNum:99000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:100000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:10671",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:11110",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:11515151",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:188889851",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:200000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:22221",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:22224",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:22225",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:28985",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:2898555",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:289855555",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:2898588",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:28991",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:28997",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:28999",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:300000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:33133",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:33331",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:33335",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:33336",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:400000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:4444344",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:444444",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:500000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:52033991",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:555555",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:58686",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:600000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:62000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:67777",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:68686",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:700000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:78888",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:800000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:82000",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:888888",
                                "value": 1
                            },
                            {
                                "source": "QunNum:988810",
                                "target": "QQNum:900000",
                                "value": 1
                            }
                        ],
                        "nodes": [
                            {
                                "id": "QQNum:100000",
                                "key": "QQNum",
                                "label": "QQNum:100000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ffff00",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QunNum:20025566",
                                "key": "QQNum",
                                "label": "QunNum:20025566",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ff4081",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "rect",
                                "value": "100000"
                            },
                            {
                                "id": "QunNum:20059682",
                                "key": "QQNum",
                                "label": "QunNum:20059682",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ff4081",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "rect",
                                "value": "100000"
                            },
                            {
                                "id": "QunNum:30084997",
                                "key": "QQNum",
                                "label": "QunNum:30084997",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ff4081",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "rect",
                                "value": "100000"
                            },
                            {
                                "id": "QunNum:932145",
                                "key": "QQNum",
                                "label": "QunNum:932145",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ff4081",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "rect",
                                "value": "100000"
                            },
                            {
                                "id": "QunNum:988810",
                                "key": "QQNum",
                                "label": "QunNum:988810",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#ff4081",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "rect",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:109320460",
                                "key": "QQNum",
                                "label": "QQNum:109320460",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11011069",
                                "key": "QQNum",
                                "label": "QQNum:11011069",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:114824187",
                                "key": "QQNum",
                                "label": "QQNum:114824187",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:116136342",
                                "key": "QQNum",
                                "label": "QQNum:116136342",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:120733347",
                                "key": "QQNum",
                                "label": "QQNum:120733347",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:121340463",
                                "key": "QQNum",
                                "label": "QQNum:121340463",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:125036152",
                                "key": "QQNum",
                                "label": "QQNum:125036152",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:130004600",
                                "key": "QQNum",
                                "label": "QQNum:130004600",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:13108757",
                                "key": "QQNum",
                                "label": "QQNum:13108757",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:251153128",
                                "key": "QQNum",
                                "label": "QQNum:251153128",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:26590802",
                                "key": "QQNum",
                                "label": "QQNum:26590802",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:26659440",
                                "key": "QQNum",
                                "label": "QQNum:26659440",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:27201048",
                                "key": "QQNum",
                                "label": "QQNum:27201048",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33032130",
                                "key": "QQNum",
                                "label": "QQNum:33032130",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:34460511",
                                "key": "QQNum",
                                "label": "QQNum:34460511",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:34781859",
                                "key": "QQNum",
                                "label": "QQNum:34781859",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:35783511",
                                "key": "QQNum",
                                "label": "QQNum:35783511",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:39928570",
                                "key": "QQNum",
                                "label": "QQNum:39928570",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:405915576",
                                "key": "QQNum",
                                "label": "QQNum:405915576",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:41131998",
                                "key": "QQNum",
                                "label": "QQNum:41131998",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:41636634",
                                "key": "QQNum",
                                "label": "QQNum:41636634",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:42295287",
                                "key": "QQNum",
                                "label": "QQNum:42295287",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:442190990",
                                "key": "QQNum",
                                "label": "QQNum:442190990",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:450459444",
                                "key": "QQNum",
                                "label": "QQNum:450459444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:453406757",
                                "key": "QQNum",
                                "label": "QQNum:453406757",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:45869842",
                                "key": "QQNum",
                                "label": "QQNum:45869842",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:46441534",
                                "key": "QQNum",
                                "label": "QQNum:46441534",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:47637682",
                                "key": "QQNum",
                                "label": "QQNum:47637682",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:47806092",
                                "key": "QQNum",
                                "label": "QQNum:47806092",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:48999402",
                                "key": "QQNum",
                                "label": "QQNum:48999402",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:49023633",
                                "key": "QQNum",
                                "label": "QQNum:49023633",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:51731123",
                                "key": "QQNum",
                                "label": "QQNum:51731123",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:520039345",
                                "key": "QQNum",
                                "label": "QQNum:520039345",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55790383",
                                "key": "QQNum",
                                "label": "QQNum:55790383",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:563477417",
                                "key": "QQNum",
                                "label": "QQNum:563477417",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:57143487",
                                "key": "QQNum",
                                "label": "QQNum:57143487",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:57296897",
                                "key": "QQNum",
                                "label": "QQNum:57296897",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:57545731",
                                "key": "QQNum",
                                "label": "QQNum:57545731",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:57602236",
                                "key": "QQNum",
                                "label": "QQNum:57602236",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:75492822",
                                "key": "QQNum",
                                "label": "QQNum:75492822",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:764731426",
                                "key": "QQNum",
                                "label": "QQNum:764731426",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:76885152",
                                "key": "QQNum",
                                "label": "QQNum:76885152",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:7789513",
                                "key": "QQNum",
                                "label": "QQNum:7789513",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:85537545",
                                "key": "QQNum",
                                "label": "QQNum:85537545",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:879504324",
                                "key": "QQNum",
                                "label": "QQNum:879504324",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:8833250",
                                "key": "QQNum",
                                "label": "QQNum:8833250",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:888888",
                                "key": "QQNum",
                                "label": "QQNum:888888",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:970190109",
                                "key": "QQNum",
                                "label": "QQNum:970190109",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:99328126",
                                "key": "QQNum",
                                "label": "QQNum:99328126",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:243485682",
                                "key": "QQNum",
                                "label": "QQNum:243485682",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:285306062",
                                "key": "QQNum",
                                "label": "QQNum:285306062",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:330219985",
                                "key": "QQNum",
                                "label": "QQNum:330219985",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:345279146",
                                "key": "QQNum",
                                "label": "QQNum:345279146",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:346093802",
                                "key": "QQNum",
                                "label": "QQNum:346093802",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:379034431",
                                "key": "QQNum",
                                "label": "QQNum:379034431",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:415879901",
                                "key": "QQNum",
                                "label": "QQNum:415879901",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:504523551",
                                "key": "QQNum",
                                "label": "QQNum:504523551",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:516822314",
                                "key": "QQNum",
                                "label": "QQNum:516822314",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:517398439",
                                "key": "QQNum",
                                "label": "QQNum:517398439",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:532272331",
                                "key": "QQNum",
                                "label": "QQNum:532272331",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:640595342",
                                "key": "QQNum",
                                "label": "QQNum:640595342",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:654014044",
                                "key": "QQNum",
                                "label": "QQNum:654014044",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:75812591",
                                "key": "QQNum",
                                "label": "QQNum:75812591",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:762133202",
                                "key": "QQNum",
                                "label": "QQNum:762133202",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:200000",
                                "key": "QQNum",
                                "label": "QQNum:200000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:200730082",
                                "key": "QQNum",
                                "label": "QQNum:200730082",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:200892613",
                                "key": "QQNum",
                                "label": "QQNum:200892613",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:243508740",
                                "key": "QQNum",
                                "label": "QQNum:243508740",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:26919126",
                                "key": "QQNum",
                                "label": "QQNum:26919126",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:294404987",
                                "key": "QQNum",
                                "label": "QQNum:294404987",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:297183460",
                                "key": "QQNum",
                                "label": "QQNum:297183460",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:300000",
                                "key": "QQNum",
                                "label": "QQNum:300000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:308015274",
                                "key": "QQNum",
                                "label": "QQNum:308015274",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:337934627",
                                "key": "QQNum",
                                "label": "QQNum:337934627",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:343937090",
                                "key": "QQNum",
                                "label": "QQNum:343937090",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:393391583",
                                "key": "QQNum",
                                "label": "QQNum:393391583",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:397678912",
                                "key": "QQNum",
                                "label": "QQNum:397678912",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:400000",
                                "key": "QQNum",
                                "label": "QQNum:400000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:408934138",
                                "key": "QQNum",
                                "label": "QQNum:408934138",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:491828974",
                                "key": "QQNum",
                                "label": "QQNum:491828974",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:500000",
                                "key": "QQNum",
                                "label": "QQNum:500000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:525321435",
                                "key": "QQNum",
                                "label": "QQNum:525321435",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:532998334",
                                "key": "QQNum",
                                "label": "QQNum:532998334",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:546054621",
                                "key": "QQNum",
                                "label": "QQNum:546054621",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:549384276",
                                "key": "QQNum",
                                "label": "QQNum:549384276",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:584643897",
                                "key": "QQNum",
                                "label": "QQNum:584643897",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:598733008",
                                "key": "QQNum",
                                "label": "QQNum:598733008",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:600000",
                                "key": "QQNum",
                                "label": "QQNum:600000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:644723605",
                                "key": "QQNum",
                                "label": "QQNum:644723605",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:700000",
                                "key": "QQNum",
                                "label": "QQNum:700000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:739983900",
                                "key": "QQNum",
                                "label": "QQNum:739983900",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:748139333",
                                "key": "QQNum",
                                "label": "QQNum:748139333",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:758810096",
                                "key": "QQNum",
                                "label": "QQNum:758810096",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:800000",
                                "key": "QQNum",
                                "label": "QQNum:800000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:807922095",
                                "key": "QQNum",
                                "label": "QQNum:807922095",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:815751507",
                                "key": "QQNum",
                                "label": "QQNum:815751507",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:819579741",
                                "key": "QQNum",
                                "label": "QQNum:819579741",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:823860591",
                                "key": "QQNum",
                                "label": "QQNum:823860591",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:83663647",
                                "key": "QQNum",
                                "label": "QQNum:83663647",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:857066092",
                                "key": "QQNum",
                                "label": "QQNum:857066092",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:900000",
                                "key": "QQNum",
                                "label": "QQNum:900000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10000000",
                                "key": "QQNum",
                                "label": "QQNum:10000000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:100001",
                                "key": "QQNum",
                                "label": "QQNum:100001",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10271",
                                "key": "QQNum",
                                "label": "QQNum:10271",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10817",
                                "key": "QQNum",
                                "label": "QQNum:10817",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10916",
                                "key": "QQNum",
                                "label": "QQNum:10916",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10927",
                                "key": "QQNum",
                                "label": "QQNum:10927",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10937",
                                "key": "QQNum",
                                "label": "QQNum:10937",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11110",
                                "key": "QQNum",
                                "label": "QQNum:11110",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11114",
                                "key": "QQNum",
                                "label": "QQNum:11114",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11213",
                                "key": "QQNum",
                                "label": "QQNum:11213",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11999",
                                "key": "QQNum",
                                "label": "QQNum:11999",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:1234567",
                                "key": "QQNum",
                                "label": "QQNum:1234567",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:14444",
                                "key": "QQNum",
                                "label": "QQNum:14444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:21111",
                                "key": "QQNum",
                                "label": "QQNum:21111",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:22221",
                                "key": "QQNum",
                                "label": "QQNum:22221",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:22224",
                                "key": "QQNum",
                                "label": "QQNum:22224",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:22225",
                                "key": "QQNum",
                                "label": "QQNum:22225",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:30303030",
                                "key": "QQNum",
                                "label": "QQNum:30303030",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33331",
                                "key": "QQNum",
                                "label": "QQNum:33331",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33332",
                                "key": "QQNum",
                                "label": "QQNum:33332",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33334",
                                "key": "QQNum",
                                "label": "QQNum:33334",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33335",
                                "key": "QQNum",
                                "label": "QQNum:33335",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33336",
                                "key": "QQNum",
                                "label": "QQNum:33336",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33337",
                                "key": "QQNum",
                                "label": "QQNum:33337",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33338",
                                "key": "QQNum",
                                "label": "QQNum:33338",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:37777",
                                "key": "QQNum",
                                "label": "QQNum:37777",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:43210",
                                "key": "QQNum",
                                "label": "QQNum:43210",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44000",
                                "key": "QQNum",
                                "label": "QQNum:44000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44440",
                                "key": "QQNum",
                                "label": "QQNum:44440",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44441",
                                "key": "QQNum",
                                "label": "QQNum:44441",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:444444",
                                "key": "QQNum",
                                "label": "QQNum:444444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44445",
                                "key": "QQNum",
                                "label": "QQNum:44445",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44446",
                                "key": "QQNum",
                                "label": "QQNum:44446",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44447",
                                "key": "QQNum",
                                "label": "QQNum:44447",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:44448",
                                "key": "QQNum",
                                "label": "QQNum:44448",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:45555",
                                "key": "QQNum",
                                "label": "QQNum:45555",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:49999",
                                "key": "QQNum",
                                "label": "QQNum:49999",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:51111",
                                "key": "QQNum",
                                "label": "QQNum:51111",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:54444",
                                "key": "QQNum",
                                "label": "QQNum:54444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55551",
                                "key": "QQNum",
                                "label": "QQNum:55551",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55552",
                                "key": "QQNum",
                                "label": "QQNum:55552",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55554",
                                "key": "QQNum",
                                "label": "QQNum:55554",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:555555",
                                "key": "QQNum",
                                "label": "QQNum:555555",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55556",
                                "key": "QQNum",
                                "label": "QQNum:55556",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55557",
                                "key": "QQNum",
                                "label": "QQNum:55557",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:55588",
                                "key": "QQNum",
                                "label": "QQNum:55588",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:619951999",
                                "key": "QQNum",
                                "label": "QQNum:619951999",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:62222",
                                "key": "QQNum",
                                "label": "QQNum:62222",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:64444",
                                "key": "QQNum",
                                "label": "QQNum:64444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:65432",
                                "key": "QQNum",
                                "label": "QQNum:65432",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:66661",
                                "key": "QQNum",
                                "label": "QQNum:66661",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:66663",
                                "key": "QQNum",
                                "label": "QQNum:66663",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:66667",
                                "key": "QQNum",
                                "label": "QQNum:66667",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:66669",
                                "key": "QQNum",
                                "label": "QQNum:66669",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:67777",
                                "key": "QQNum",
                                "label": "QQNum:67777",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:71111",
                                "key": "QQNum",
                                "label": "QQNum:71111",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:72222",
                                "key": "QQNum",
                                "label": "QQNum:72222",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:73333",
                                "key": "QQNum",
                                "label": "QQNum:73333",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:74444",
                                "key": "QQNum",
                                "label": "QQNum:74444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77770",
                                "key": "QQNum",
                                "label": "QQNum:77770",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77771",
                                "key": "QQNum",
                                "label": "QQNum:77771",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77772",
                                "key": "QQNum",
                                "label": "QQNum:77772",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77773",
                                "key": "QQNum",
                                "label": "QQNum:77773",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77775",
                                "key": "QQNum",
                                "label": "QQNum:77775",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77776",
                                "key": "QQNum",
                                "label": "QQNum:77776",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77778",
                                "key": "QQNum",
                                "label": "QQNum:77778",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:77779",
                                "key": "QQNum",
                                "label": "QQNum:77779",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:78888",
                                "key": "QQNum",
                                "label": "QQNum:78888",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:81111",
                                "key": "QQNum",
                                "label": "QQNum:81111",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:82222",
                                "key": "QQNum",
                                "label": "QQNum:82222",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:83333",
                                "key": "QQNum",
                                "label": "QQNum:83333",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:84444",
                                "key": "QQNum",
                                "label": "QQNum:84444",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:85630",
                                "key": "QQNum",
                                "label": "QQNum:85630",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:88788",
                                "key": "QQNum",
                                "label": "QQNum:88788",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:88800",
                                "key": "QQNum",
                                "label": "QQNum:88800",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:88884",
                                "key": "QQNum",
                                "label": "QQNum:88884",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:88885",
                                "key": "QQNum",
                                "label": "QQNum:88885",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:88887",
                                "key": "QQNum",
                                "label": "QQNum:88887",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:92222",
                                "key": "QQNum",
                                "label": "QQNum:92222",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:99000",
                                "key": "QQNum",
                                "label": "QQNum:99000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:10671",
                                "key": "QQNum",
                                "label": "QQNum:10671",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:11515151",
                                "key": "QQNum",
                                "label": "QQNum:11515151",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:188889851",
                                "key": "QQNum",
                                "label": "QQNum:188889851",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:28985",
                                "key": "QQNum",
                                "label": "QQNum:28985",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:2898555",
                                "key": "QQNum",
                                "label": "QQNum:2898555",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:289855555",
                                "key": "QQNum",
                                "label": "QQNum:289855555",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:2898588",
                                "key": "QQNum",
                                "label": "QQNum:2898588",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:28991",
                                "key": "QQNum",
                                "label": "QQNum:28991",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:28997",
                                "key": "QQNum",
                                "label": "QQNum:28997",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:28999",
                                "key": "QQNum",
                                "label": "QQNum:28999",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:33133",
                                "key": "QQNum",
                                "label": "QQNum:33133",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:4444344",
                                "key": "QQNum",
                                "label": "QQNum:4444344",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:52033991",
                                "key": "QQNum",
                                "label": "QQNum:52033991",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:58686",
                                "key": "QQNum",
                                "label": "QQNum:58686",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:62000",
                                "key": "QQNum",
                                "label": "QQNum:62000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:68686",
                                "key": "QQNum",
                                "label": "QQNum:68686",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            },
                            {
                                "id": "QQNum:82000",
                                "key": "QQNum",
                                "label": "QQNum:82000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "style": {
                                    "fill": "#18ffff",
                                    "opacity": [
                                        0.8
                                    ]
                                },
                                "type": "circle",
                                "value": "100000"
                            }
                        ]
                    }
                },
                resu: {
                    "code": 200,
                    "msg": "successful!",
                    "result_data": {
                        "edges": [
                        ],
                        "nodes": [
                        ]
                    }
                },
                QQNum: "",
                QunNum: "",
                error: false,
                data: [
                    {genre: "Sports", sold: 275},
                    {genre: "Strategy", sold: 115},
                    {genre: "Action", sold: 120},
                    {genre: "Shooter", sold: 350},
                    {genre: "Other", sold: 150}
                ]
            };
        },
        methods: {
            init() {
                let that = this
                that.leading = true
                that.happy = false
                that.error = false
                that.result.code = 400
            },
            posturl() {
                let that = this
                that.leading = true
                that.happy = false
                that.error = false
                that.result.code = 400
                var key = ""
                var value = ""
                console.log(that.QQNum,that.QunNum)
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
                this.axios.post(that.globalHttpUrl + 'v/antv/', {
                    "key": key,
                    "value": value
                }).then((response) => {
                    if (response.data.code === 200) {
                        console.log(response.data)
                        that.result = response.data
                        // this.initComponent()

                        this.resu = this.result
                        this.graph.clear()
                        const graph = this.graph
                        var data = this.result.result_data
                        console.log(data)
                        const nodes = data.nodes;
                        // randomize the node size
                        nodes.forEach((node) => {
                            node.size = 15;
                        });
                        graph.data({
                            nodes,
                            edges: data.edges.map(function (edge, i) {
                                edge.id = 'edge' + i;
                                return Object.assign({}, edge);
                            }),
                        });
                        graph.render();

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
            },
            initComponent() {
                const container = document.getElementById('container');
                const width = container.scrollWidth;
                const height = container.scrollHeight || 500;
                const graph = new G6.Graph({
                    defaultNode: {

                        labelCfg: {
                            // 节点上的标签文本样式配置
                            style: {

                                fontSize: 0,
                            },
                        },
                    },
                    defaultEdge: {
                        style: {
                            opacity: 1.0, // 边透明度
                            stroke: '#ff4757', // 边描边颜色
                        },
                    },
                    container: 'container',
                    width,
                    height,
                    layout: {
                        type: 'force',
                        preventOverlap: true,
                    },
                    modes: {
                        default: [
                            'drag-canvas',
                            {
                                type: 'tooltip', // 提示框
                                formatText(model) {
                                    // console.log(model.label)
                                    // 提示框文本内容
                                    const text = model.label;
                                    return text;
                                },
                            },
                        ],
                    },
                });
                let that = this
                var data = that.resu.result_data
                console.log(data)
                const nodes = data.nodes;
                // randomize the node size
                nodes.forEach((node) => {
                    node.size = 15;
                });
                graph.data({
                    nodes,
                    edges: data.edges.map(function (edge, i) {
                        edge.id = 'edge' + i;
                        return Object.assign({}, edge);
                    }),
                });
                graph.render();

                const forceLayout = graph.get('layoutController').layoutMethod;

                graph.on('node:dragstart', function (e) {
                    graph.layout();
                    refreshDragedNodePosition(e);
                });
                graph.on('node:drag', function (e) {
                    forceLayout.execute();
                    refreshDragedNodePosition(e);
                });
                graph.on('node:dragend', function (e) {
                    e.item.get('model').fx = null;
                    e.item.get('model').fy = null;
                });
                graph.on('node:dblclick', function (e) {
                    console.log(e.item)
                    var id = e.item.get('id')
                    console.log(id)
                    var word = id.split(":")
                    console.log(word[0])
                    if (word[0] === "QQNum"){
                        that.QQNum = word[1]
                        that.QunNum = ""
                    }else {
                        that.QunNum = word[1]
                        that.QQNum = ""
                    }
                    console.log("$$$$4",that.QQNum,that.QunNum)
                    that.posturl()


                });


                if (typeof window !== 'undefined')
                    window.onresize = () => {
                        if (!graph || graph.get('destroyed')) return;
                        if (!container || !container.scrollWidth || !container.scrollHeight) return;
                        graph.changeSize(container.scrollWidth, container.scrollHeight);
                    };

                function refreshDragedNodePosition(e) {
                    const model = e.item.get('model');
                    model.fx = e.x;
                    model.fy = e.y;
                }

                return graph
            }
        }
    }
    ;
</script>
<style>
    /* 提示框的样式 */
    .g6-tooltip {
        border: 1px solid #e2e2e2;
        border-radius: 4px;
        font-size: 12px;
        color: #545454;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px 8px;
        box-shadow: rgb(174, 174, 174) 0px 0px 10px;
    }
</style>