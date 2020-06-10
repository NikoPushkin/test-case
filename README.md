# test-case
<h1>Django-application with extended user-model, payout and payment models and extended admin-inteface</h1>

<ul><h3>This application has a follow functionality:</h3>
  <li>create extened user-profile</li>
  <li>commit payments and payouts, what influences on the user-balance</li>
  <li>custom-actions for working with payout-objects in admin panel
  (change payout-status for concrete payouts or for all of them)</li>
</ul>

<h4>True payout-status changing leds to creation of confirmation-date, prohibits further modification of the payment-object and
withdraws money from user account.</h4>

<h4>There is a createPayment function in services, which accepts profile id and sum of replenishement
and lets to create new payment and replenish user-balance.</h4>
