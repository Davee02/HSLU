# Global Harmony App Inventor Project

## Values saved in TinyDB

| Key              | Description / format                                                                                                                                                                                    | Initialized in screen |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `AuthToken`      | The ID token for the google identitykit                                                                                                                                                                 | `SignUp`              |
| `MyAccountData`  | The JSON object of the current logged in user, loaded from firebase DB (`GET https://globalharmony-39de6-default-rtdb.europe-west1.firebasedatabase.app/users.json?orderBy="uid"&equalTo="[USER UID]"`) | `Swiper`              |
| `AllAccountData` | All users from the firebase DB as a JSON array (`GET https://globalharmony-39de6-default-rtdb.europe-west1.firebasedatabase.app/users.json`)                                                            | `Swiper`              |

## Changelog

| Date / Time    | Who? | What?                                                                                  |
| -------------- | ---- | -------------------------------------------------------------------------------------- |
| 04.06.23 21:00 | Deif | Added swiper logic (UI still pending), gave buttons & labels better names on all views |

## Good to know

- The login function is not implemented yet, so you can't use an existing account. You can however use the `SignUp` screen to create a new account. Because App Inventor is a fucking piece of shit the connection to the companion app sometimes stops working and the app's data is reset, so you have to create a new account.
