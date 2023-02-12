import '../App.css';
import Logo from '../images/logo.png'
export default function(){
    return(
        <div className="login">
            <img src={Logo} alt="Lms"></img>
            <form>
                <div>
                    <label>Email</label>
                    <input name="email " type="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-2.5 px-5 dark:bg-blue-500 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder='Email'></input>
                </div>
                <div className='pass'>
                    <label>Password</label>
                    <input name="password" type="password" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-2.5 px-4 dark:bg-blue-500 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder='Password'></input>
                    <a href=''>Forget Password?</a>
                </div>
                <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-9 border border-blue-500 hover:border-transparent rounded mt-6" >Submit</button>
            </form>
        </div>
    )
}