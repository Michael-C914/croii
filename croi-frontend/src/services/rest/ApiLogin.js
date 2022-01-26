import apiRest from "../AxiosInstance";
export const loginApp = async (user, email) => {
	return apiRest.post("/user/api/token/", {
		password: email,
		email: user
	}, {
		headers: {
			accept: '*/*',
			'Content-Type': 'application/json'
		}
	})
}