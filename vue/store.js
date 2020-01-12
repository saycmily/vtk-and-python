import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    studentId: 1,
    count: 0,
    grade: 0,
    oldpassword: '1',
    bookId: 1,
    spellNumber: 1,
    lastscore: '?',
    showbutton: false,
    percentnum: 0
  },
  mutations: {
    setStudentId (state, studentId) {
      state.studentId = studentId
      sessionStorage.setItem('studentId', studentId)
    },
    setShowbutton (state, showbutton) {
      state.showbutton = showbutton
      sessionStorage.setItem('showbutton', showbutton)
    },
    setPercentnum (state, percentnum) {
      state.percentnum = percentnum
      sessionStorage.setItem('percentnum', percentnum)
    },
    setlastscore (state, lastscore) {
      state.lastscore = lastscore
      sessionStorage.setItem('lastscore', lastscore)
    },
    setoldpassword (state, oldpassword) {
      state.oldpassword = oldpassword
      sessionStorage.setItem('oldpassword', oldpassword)
    },
    setbookId (state, bookId) {
      state.bookId = bookId
      sessionStorage.setItem('bookId', bookId)
    },
    setspellNumber (state, spellNumber) {
      state.spellNumber = spellNumber
      sessionStorage.setItem('spellNumber', spellNumber)
    },
    setCount (state, count) {
      state.count = count
      sessionStorage.setItem('count', count)
    },
    setGrade (state, grade) {
      state.grade = grade
      sessionStorage.setItem('grade', grade)
    }
  },
  getter: {
    studentId: (state) => sessionStorage.getItem('studentId'),
    showbutton: (state) => sessionStorage.getItem('showbutton'),
    lastscore: (state) => sessionStorage.getItem('lastscore'),
    oldpassword: (state) => sessionStorage.getItem('oldpassword'),
    bookId: (state) => sessionStorage.getItem('bookId'),
    spellNumber: (state) => sessionStorage.getItem('spellNumber'),
    count: (state) => sessionStorage.getItem('count'),
    grade: (state) => sessionStorage.getItem('grade'),
    percentnum: (state) => sessionStorage.getItem('percentnum')
  }
})