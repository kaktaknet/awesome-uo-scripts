using System;
using System.Collections;
using Server.Items;
using Server.Targeting;

namespace Server.Mobiles
{
	public class Three : BaseCreature
	{
		public override bool ShowFameTitle{ get{ return false; } }
		private static bool m_Talked;

		string[] kfcsay = new string[]
		{
		"You have no idea what my master can do!",
		"Have you prayed toy our gods today!",
		"You wont defeat me so easily!",
		"Your soul will be ours!",
		"Come at me with all you have mortal!",
		"I see you have friends with you, they're nothing but more mortals!",
		};

		[Constructable]
		public Three() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.4, 0.8 )
		{
			Name = "Guardian of Sethrodemus";
			Body = 0x2EA;
			Hue = 0x0;
			BaseSoundID = 357;

			SetStr( 400, 600 );
			SetDex( 120, 155 );
			SetInt( 100, 200 );

			SetHits( 8000, 12000 );

			SetDamage( 15, 20 );

			SetDamageType( ResistanceType.Physical, 100 );

			SetResistance( ResistanceType.Physical, 60, 65 );
			SetResistance( ResistanceType.Fire, 65, 65 );
			SetResistance( ResistanceType.Cold, 65, 65 );
			SetResistance( ResistanceType.Poison, 65, 65 );
			SetResistance( ResistanceType.Energy, 65, 65 );

			SetSkill( SkillName.MagicResist, 110.1, 120.0 );
			SetSkill( SkillName.Swords, 120.1, 130.0 );
			SetSkill( SkillName.Tactics, 120.1, 130.0 );
			SetSkill( SkillName.Wrestling, 120.1, 130.0 );

			Fame = 15000;
			Karma = -15000;

			VirtualArmor = 55;

			PackGold( 5000, 15000 );
			PackScroll( 2, 8 );
			PackArmor( 2, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 5, 5 );
			PackArmor( 2, 5 );
			PackArmor( 2, 5 );
			PackArmor( 2, 5 );
			PackArmor( 2, 5 );
			PackArmor( 2, 5 );
			PackWeapon( 3, 5 );
			PackWeapon( 5, 5 );
			PackArmor( 2, 5 );
			PackSlayer();
		}

		public override bool AlwaysAttackable{ get{ return true; } }
		public override bool AlwaysMurderer{ get{ return true; } }
		public override bool Unprovokable{ get{ return true; } }
		public override bool Uncalmable{ get{ return true; } }
		public override Poison PoisonImmune{ get{ return Poison.Lethal; } }

		public override int GetDeathSound()
		{
			return 0x2CD;
		}

		public Three( Serial serial ) : base( serial )
		{
		}
		
		public override void OnMovement( Mobile m, Point3D oldLocation ) 
               {                                                    
         		if( m_Talked == false ) 
        		 { 
          		 	 if ( m.InRange( this, 4 ) ) 
          			  {                
          				m_Talked = true; 
              				SayRandom( kfcsay, this ); 
				this.Move( GetDirectionTo( m.Location ) ); 
				SpamTimer t = new SpamTimer(); 
				t.Start(); 
            			} 
		} 
	} 

	private class SpamTimer : Timer 
	{ 
		public SpamTimer() : base( TimeSpan.FromSeconds( 15 ) ) 
		{ 
			Priority = TimerPriority.OneSecond; 
		} 

		protected override void OnTick() 
		{ 
		m_Talked = false; 
		} 
	} 

	private static void SayRandom( string[] say, Mobile m ) 
	{ 
		m.Say( say[Utility.Random( say.Length )] ); 
	}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );
			writer.Write( (int) 0 );
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );
			int version = reader.ReadInt();
		}
	}
}