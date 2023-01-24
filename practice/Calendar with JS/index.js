const date = new Date();

const makeCalendar = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  //년도 달 채우기
  document.querySelector(".year-month").textContent = `${viewYear}년 ${
    viewMonth + 1
  }월`;

  //이전 달 마지막 날짜 가져오기
  const prevLast = new Date(viewYear, viewMonth, 0);
  const prevDate = prevLast.getDate();
  const prevDay = prevLast.getDay();

  //이번 달 마지막 날짜 가져오기
  const thisLast = new Date(viewYear, viewMonth + 1, 0);
  const thisDate = thisLast.getDate();
  const thisDay = thisLast.getDay();

  //전체 달력에 필요한 날짜들을 만들어 주기 위한 배열
  const prevDates = [];
  const thisDates = [...Array(thisDate + 1).keys()].slice(1);
  const nextDates = [];

  //prevDates 계산
  if (prevDay !== 6) {
    for (let i = 0; i < prevDay + 1; i++) {
      prevDates.unshift(prevDate - i);
    }
  }

  //nextDates 계산
  for (let i = 1; i < 7 - thisDay; i++) {
    nextDates.push(i);
  }

  //Dates 합치기
  const dates = prevDates.concat(thisDates, nextDates);

  dates.forEach((date, i) => {
    dates[i] = `<div class="date">${date}</div>`;
  });

  //Dates 그리기
  document.querySelector(".dates").innerHTML = dates.join("");
};
