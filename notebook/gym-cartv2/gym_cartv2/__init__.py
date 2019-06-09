from gym.envs.registration import register

register(
    id='cart-v2',
    entry_point='gym_cartv2.envs:Cart2',
)
