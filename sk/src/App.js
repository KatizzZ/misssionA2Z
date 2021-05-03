// import logo from './logo.svg';
import "./App.css";
const divStyle = {
  backgroundImage: `url(${"https://i.kym-cdn.com/photos/images/original/001/231/999/ba5.jpg"})`,
  backgroundPosition: "center",
  // backgroundSize: 'cover',
  backgroundRepeat: "no-repeat",
  width: "100vw",
  height: "100vh",
  overflow: "hidden"
};
function App() {
  return (
    <div className="App" style={divStyle}>
      <header>
        <p style={{ "font-size": "80px", color:'red', 'text-align':'center'}}>
          1667399.00DR
          <a
            className="App-link"
            href="https://www.indianbank.net.in/jsp/startIB.jsp"
            target="_blank"
            rel="noopener noreferrer"
          >
            <div> </div> Time to Pay Debt to Motherland
          </a>
        </p>
      </header>
    </div>
  );
}

export default App;
