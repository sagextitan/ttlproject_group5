const React = require('react');
const ReactDOM = require('react-dom');

function App() {
  const [count, setCount] = React.useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

module.exports = {
  App,
  React,
  ReactDOM
};
