import React, { Component } from 'react';
import ListAulas from './components/ListAulas';
import Aula from './components/Aula';
import { BrowserRouter as Router, Route, Link, Redirect } from "react-router-dom";

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={ListAulas} />
          <Route exact path="/aulas" component={ListAulas} />
          <Route path="/aulas/:id" component={Aula} />
        </div>
      </Router>
    );
  }
}

export default App;