import React from 'react';
import logo from './trends_logo.png';
import './App.css';

import SearchField from './components/SearchField';

import { VictoryBar, VictoryLine, VictoryChart } from 'victory';

import googleTrends from 'google-trends-api';
 
const data = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

function App() {

  const [interestOverTimeData, setInterestOverTimeData] = React.useState(data);

  function getInterestOverTime(keyword){

    saveKeywordToDatabase(keyword);

    googleTrends.interestOverTime({keyword: keyword, startTime: new Date('2018'), endTime: new Date()},
    (err, results) => {
      if(err) {
        alert("Error looking for "+keyword+", "+err);
        console.error('there was an error!', err);
      }
      else console.log('my sweet sweet results', results);
      //setInterestOverTimeData(receivedData);
    })
  }

  function saveKeywordToDatabase(keyword){
    // TODO write function that saves the keyword to your internal database
  }

  return (
    <div className="App">
      <header className="App-header">

        <img src={logo} className="App-logo" alt="logo" />
        {/*        
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>*/}
        <SearchField onClick={(keyword) => getInterestOverTime(keyword)}/>
      </header>

      <div style={{display:'flex', flexDirection:'row'}}>
        <div style={{width:'50vw'}}>
          <VictoryChart>
            <VictoryBar
              data={interestOverTimeData}
              x="quarter"
              y="earnings"
            />
          </VictoryChart>
          </div>
          <div style={{width:'50vw'}}>
            <VictoryChart>
              <VictoryLine
                data={interestOverTimeData}
                x="quarter"
                y="earnings"
              />
            </VictoryChart>
        </div>
      </div>
      <div>
        <VictoryChart>
          <VictoryLine
            data={interestOverTimeData}
            x="quarter"
            y="earnings"
          />
        </VictoryChart>
      </div>
    </div>
  );
}

export default App;
