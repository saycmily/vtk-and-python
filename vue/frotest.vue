<template>
<div id="box1">
    <button class="btns_1" @click="switchb">{{'切换单词书'}}</button>
    <img src="~@/../static/images/flag.jpg" alt="" id="froflag">
    <label for="" id="frotitle">学前检测</label>
    <!-- <input type="text" id="examination_num" placeholder="（计划检测99题）" readonly> -->
    <label for="" id="examination_num">{{'（计划检测' + examinationnums + '题）'}}</label>
    <div id="line"></div>
    <div class="examination">
        <div for="" class="firstexamination">{{signnum+'.'+eng_1}}</div>
        <div class="firstopition" @click="firstopition_1" :class="{normal: chose_11,blue: !chose_11}">{{selections_1[0]}}</div>
        <div class="secondopition" @click="secondopition_1" :class="{normal: chose_12,blue: !chose_12}">{{selections_1[1]}}</div>
        <div class="secondopition" @click="thirdopition_1" :class="{normal: chose_13,blue: !chose_13}">{{selections_1[2]}}</div>
        <div class="secondopition" @click="forthopition_1" :class="{normal: chose_14,blue: !chose_14}">{{selections_1[3]}}</div>
    </div>
    <div class="examination">
        <div for="" class="firstexamination">{{signnum+1+'.'+eng_2}}</div>
        <div class="firstopition" @click="firstopition_2" :class="{normal: chose_21,blue: !chose_21}">{{selections_2[0]}}</div>
        <div class="secondopition" @click="secondopition_2" :class="{normal: chose_22,blue: !chose_22}">{{selections_2[1]}}</div>
        <div class="secondopition" @click="thirdopition_2" :class="{normal: chose_23,blue: !chose_23}">{{selections_2[2]}}</div>
        <div class="secondopition" @click="forthopition_2" :class="{normal: chose_24,blue: !chose_24}">{{selections_2[3]}}</div>
    </div>
    <button id="next" @click="next">{{message_1}}</button>
    <div v-if="showpop" id="becomegray"></div>
    <div v-if="showpop" id="pop">
        <img src="~@/../static/images/nextimg.png" alt="" id="nextimg">
        <label for="" id="nextgo">{{message_2}}</label>
        <button id="golearn" @click="golearn">{{'继续学习'}}</button>
    </div>
</div>
</template>

<script>
// import Bus from 'busa.js'
export default {
  name: 'frotest',
  data () {
    return {
      chose_11: true,
      chose_12: true,
      chose_13: true,
      chose_14: true,
      chose_21: true,
      chose_22: true,
      chose_23: true,
      chose_24: true,
      showpop: false,
      s1: [1, 1, 1, 1],
      s2: [1, 1, 1, 1],
      selectsign: 0,
      message_1: '下一组',
      message_2: '马上进入下一回合，冲鸭！',
      signnum: 1,
      // one: [0, 0, 0, 0, 0, 0, 0, 0],
      one: 0,
      two: 0,
      isknow_1: 0,
      isknow_2: 0,
      money: 0,
      // eng: '',

      examinationnums: 0,
      froscoresign: 0,
      score: 0,
      eng_1: '',
      eng_2: '',
      yes_1: '',
      no1_1: '',
      no2_1: '',
      no3_1: '',
      yes_2: '',
      no1_2: '',
      no2_2: '',
      no3_2: '',
      selections_1: ['', '', '', ''],
      selections_2: ['', '', '', '']
    }
  },
  created () {
    this.mycreate()
  },
  methods: {
    mycreate () {
      let param = new URLSearchParams()
      let bookId = this.$store.state.bookId
      param.append('book_id', bookId)
      param.append('word_id1', this.signnum)
      param.append('word_id2', this.signnum + 1)
      this.$axios('frotest/', {
        method: 'post',
        data: param
      }).then(res => {
        this.eng_1 = res.data[0].english
        this.eng_2 = res.data[1].english
        this.examinationnums = res.data[8].examinationnums
        this.yes_1 = res.data[0].chinese
        this.no1_1 = res.data[3].chinese
        this.no2_1 = res.data[4].chinese
        this.no3_1 = res.data[5].chinese
        this.yes_2 = res.data[1].chinese
        this.no1_2 = res.data[6].chinese
        this.no2_2 = res.data[2].chinese
        this.no3_2 = res.data[7].chinese
        this.selectsign = (parseInt(Math.random() * 4))
        this.s1[this.selectsign] = 0
        this.selections_1[this.selectsign] = this.yes_1
        this.selectsign = (parseInt(Math.random() * 4))
        this.s2[this.selectsign] = 0
        this.selections_2[this.selectsign] = this.yes_2
        for (let i = 0; i < 4; i++) {
          if (this.s1[i] === 1) {
            if (this.no1_1 !== '') {
              this.selections_1[i] = this.no1_1
              this.no1_1 = ''
            } else if (this.no2_1 !== '') {
              this.selections_1[i] = this.no2_1
              this.no2_1 = ''
            } else {
              this.selections_1[i] = this.no3_1
            }
            this.s1[i] = 0
          }
        }
        for (let i = 0; i < 4; i++) {
          if (this.s2[i] === 1) {
            if (this.no1_2 !== '') {
              this.selections_2[i] = this.no1_2
              this.no1_2 = ''
            } else if (this.no2_2 !== '') {
              this.selections_2[i] = this.no2_2
              this.no2_2 = ''
            } else {
              this.selections_2[i] = this.no3_2
            }
          }
          this.s2[i] = 0
        }
      }).catch(error => console.log(error))
    },
    myknow () {
      let param = new URLSearchParams()
      let studentId = this.$store.state.studentId
      // let bookId = this.$store.state.bookId
      param.append('english1', this.eng_1)
      param.append('english2', this.eng_2)
      param.append('proValue1', this.isknow_1)
      param.append('proValue2', this.isknow_2)
      param.append('studentId', studentId)
      // param.append('bookId', bookId)
      this.$axios('procreate/', {
        method: 'post',
        data: param
      }).then(res => console.log(res.data.code)).catch(error => console.log(error))
    },
    switchb () {
      this.$router.push({name: 'switchbooks'})
    },
    choses_1 () {
      this.chose_11 = true
      this.chose_12 = true
      this.chose_13 = true
      this.chose_14 = true
    },
    choses_2 () {
      this.chose_21 = true
      this.chose_22 = true
      this.chose_23 = true
      this.chose_24 = true
    },
    firstopition_1 () {
      this.choses_1()
      this.chose_11 = false
      this.one = 1
    },
    secondopition_1 () {
      this.choses_1()
      this.chose_12 = false
      this.one = 2
    },
    thirdopition_1 () {
      this.choses_1()
      this.chose_13 = false
      this.one = 3
    },
    forthopition_1 () {
      this.choses_1()
      this.chose_14 = false
      this.one = 4
    },
    firstopition_2 () {
      this.choses_2()
      this.chose_21 = false
      this.two = 1
    },
    secondopition_2 () {
      this.choses_2()
      this.chose_22 = false
      this.two = 2
    },
    thirdopition_2 () {
      this.choses_2()
      this.chose_23 = false
      this.two = 3
    },
    myscore () {
      let param = new URLSearchParams()
      let studentId = this.$store.state.studentId
      let bookId = this.$store.state.studentId
      param.append('money', this.money)
      param.append('studentId', studentId)
      param.append('froscore', this.froscoresign)
      // param.append('isKnow', this.isknow)
      param.append('bookId', bookId)
      // param.append('spellNum', this.signnum)
      this.$axios('frotestscore/', {
        method: 'post',
        data: param
      }).then(res => {
        console.log(res.data)
      }).catch(error => console.log(error))
    },
    forthopition_2 () {
      this.choses_2()
      this.chose_24 = false
      this.two = 4
    },
    next () {
      for (let i = 0; i < 4; i++) {
        this.s1[i] = 1
        this.s2[i] = 1
      }
      this.signnum += 2
      console.log(this.signnum)
      this.showpop = true
      this.choses_1()
      this.choses_2()
      if (this.selections_1[this.one - 1] === this.yes_1 && this.one !== 0) {
        this.isknow_1 = 4
        this.money++
        this.froscoresign++
        // this.eng = this.eng_1
        // this.myscore()
        // this.myknow()
        this.score += 5
      } else {
        this.isknow_1 = 0
        // this.myknow()
      }
      this.one = 0
      if (this.selections_2[this.two - 1] === this.yes_2 && this.two !== 0) {
        this.isknow_2 = 4
        this.money++
        this.froscoresign++
        // this.eng = this.eng_2
        // console.log(this.eng)
        // this.myscore()
        // this.myknow()
        this.scorse += 5
      } else {
        // this.eng = this.eng_2
        this.isknow_2 = 0
        // this.myknow()
      }
      this.myscore()
      this.myknow()
      this.two = 0
      this.froscoresign = 0
      this.money = 0
      if (this.signnum <= this.examinationnums) {
        this.mycreate()
      }
    },
    golearn () {
      this.showpop = false
      if (this.signnum + 2 >= this.examinationnums) {
        if ((this.score / 5) / this.examinationnums >= 0.9) {
          this.message_2 = this.score + '分!你很棒'
        } else if ((this.score / 5) / this.examinationnums >= 0.6) {
          this.message_2 = this.score + '分!还需继续努力'
        } else {
          this.message_2 = this.score + '分!要加油了'
        }
      }
      if (this.signnum > this.examinationnums) {
        this.$emit('frotestmeg', false)
        // this.$emit('froscoremeg', this.score)
        // Bus.$emit('send', this.data)
      }
      if (this.signnum + 2 >= this.examinationnums) {
        this.message_1 = '提交'
      }
    }
  }
}
</script>

<style scoped>
#box1 {
  position: absolute;
  background: #ffffff;
  border-radius: 5px;
  width: 700px;
  height: 750px;
  top: 10px;
  left: 650px;
}
#froflag {
  margin-top: -150px;
  margin-left: 20px;
  width: 40px;
  height: 40px;
}
#frotitle {
    position: absolute;
    top: 28px;
    margin-left: 15px;
    font-family: Tahoma;
    font-weight: 550;
}
#examination_num {
    position: absolute;
    top: 28px;
    margin-left: 70px;
    width: 200px;
    border: 0;
    outline: none;
    font-weight: 550;
    font-size: 15px;
}
#line {
  background: #f0f0f0;
  width: 600px;
  height: 2px;
  margin-top: 20px;
  margin-left: 50px;
}
.firstexamination {
    margin-left: 20px;
    margin-top: 35px;
    border: 0;
    font-size: 16px;
    outline: none;
}
.firstopition {
    margin-top: 20px;
    margin-left: 20px;
    border-radius: 50px;
    outline: none;
    cursor: pointer;
    width: 350px;
    height: 40px;
    text-align: left;
    text-indent: 20px;
    font-size: 24px;
    color: rgb(80, 80, 80);
}
.secondopition {
    margin-top: 10px;
    margin-left: 20px;
    border-radius: 50px;
    outline: none;
    cursor: pointer;
    width: 350px;
    height: 40px;
    text-align: left;
    text-indent: 20px;
    font-size: 24px;
    color: rgb(80, 80, 80);
}
.blue {
    border: 1.5px solid rgb(0, 174, 255);
    background: rgb(155, 208, 233, 0.3);
}
.normal{
    border: 1px solid #c0c0c0;
}
#next {
  position: absolute;
  bottom: 30px;
  right: 30px;
  height: 35px;
  background: #60c268;
  /* text-align: center;
  vertical-align:auto; */
  width: 150px;
  border: 0;
  border-radius: 5px;
  color: #ffffff;
  font-weight: 550;
  cursor: pointer;
  outline: none;
}
#pop {
    position: absolute;
    top: 200px;
    left: -15px;
    height: 300px;
    width: 400px;
    background: #ffffff;
    border-radius: 10px;
}
#becomegray {
    position: absolute;
    right: -169px;
    top: -80px;
    width: 1550px;
    height: 870px;
    background: rgb(56, 56, 56, 0.4);
}
#golearn {
    position: absolute;
    bottom: 20px;
    right: 100px;
    width: 200px;
    height: 40px;
    background: #60c268;
    border-radius: 5px;
    outline: none;
    border: 0;
    cursor: pointer;
    color: #ffffff;
    font-size: 15px;
    font-weight: 600;
}
#nextgo {
    position: absolute;
    bottom: 10px;
    width: 400px;
    height: 100px;
    font-weight: 550;
    color: grey;
    text-align: center;
}
#nextimg {
    position: absolute;
    width: 400px;
    height: 200px;
}
#box1 .btns_1 {
  margin-left: 500px;
  height: 35px;
  width: 150px;
  margin-top: 30px;
  border: 0;
  border-radius: 5px;
  cursor: pointer;
  outline: none;
  font-weight: 550;
  background: #f0f0f0;
  color: #606060;
}
#box1 .btns_1:active {
  background: #06a313;
  color: #ffffff;
}
</style>
